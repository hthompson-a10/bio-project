import copy
import os
import unittest
from unittest import mock
from unittest.mock import mock_open

from bio.gtf import avl
from bio.gtf import annotate

class TestAnnotate(unittest.TestCase):

    def _format_filedata(self, lines):
        return '\n'.join(tuple(lines))

    @mock.patch('bio.gtf.avl.GeneTreeNode')
    @mock.patch('bio.gtf.annotate._create_annotation_node')
    def test_buildtreemap_empty_file(self, mock_annotation, mock_root):
        with mock.patch("builtins.open", mock_open(read_data="")) as mock_file:
            result = annotate.build_tree_map(['mock_file_path'])
        self.assertEqual(result, {})

    @mock.patch('bio.gtf.avl.GeneTreeNode')
    @mock.patch.object(avl.AVLGeneTree, 'insert')
    @mock.patch('bio.gtf.annotate._create_annotation_node')
    def test_buildtreemap_one_line(self, mock_annotation, mock_tree, mock_root):
        mock_annotation.return_value = mock.Mock(gene_name='mock_gene')
        mock_root.return_value = mock.Mock(gene_name='mock_gene', annotations=[])
        mock_lines = self._format_filedata(['line1'])
        with mock.patch("builtins.open", mock_open(read_data=mock_lines)) as mock_file:
            result = annotate.build_tree_map(['mock_file_path'])
        self.assertEqual(len(result.keys()), 1)

    @mock.patch('bio.gtf.avl.GeneTreeNode')
    @mock.patch.object(avl.AVLGeneTree, 'insert')
    @mock.patch('bio.gtf.annotate._create_annotation_node')
    def test_buildtreemap_duplicate_chromosome(self, mock_annotation, mock_tree, mock_root):
        anno_1 = mock.Mock(gene_name='mock_gene', chromosome='chr1')
        anno_2 = mock.Mock(gene_name='mock_gene', chromosome='chr1')
        mock_annotation.side_effect = [anno_1, anno_2]
        mock_lines = self._format_filedata(['line1', 'line2'])
        with mock.patch("builtins.open", mock_open(read_data=mock_lines)) as mock_file:
            result = annotate.build_tree_map(['mock_file_path'])
        self.assertEqual(len(result.keys()), 1)


    @mock.patch.object(avl.AVLGeneTree, 'insert')
    @mock.patch('bio.gtf.annotate._create_annotation_node')
    def test_buildtreemap_no_duplicate_chromosomes(self, mock_annotation, mock_tree):
        anno_1 = mock.Mock(gene_name='mock_gene', chromosome='chr1')
        anno_2 = mock.Mock(gene_name='mock_gene2', chromosome='chr2')
        mock_annotation.side_effect = [anno_1, anno_2]
        mock_lines = self._format_filedata(['line1', 'line2'])
        with mock.patch("builtins.open", mock_open(read_data=mock_lines)) as mock_file:
            result = annotate.build_tree_map(['mock_file_path'])
        self.assertEqual(len(result.keys()), 2)


class TestAnnotateIntegration(unittest.TestCase):

    def test_buildtreemap_map_has_two_entries(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        fixture_path = "../../fixtures/gtf/hg19_fixture1.gtf"
        fixture_path = os.path.join(dir_path, fixture_path)
        tree_map = annotate.build_tree_map(fixture_path)
        self.assertEqual(tree_map['chr3'].start, 134196546)
        self.assertEqual(tree_map['chr3'].end, 134204866)
        self.assertEqual(tree_map['chr9'].start, 136325087)
        self.assertEqual(tree_map['chr9'].end, 136335910)

    def test_buildtreemap_root_has_left_node(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        fixture_path = "../../fixtures/gtf/hg19_fixture2.gtf"
        fixture_path = os.path.join(dir_path, fixture_path)
        tree_map = annotate.build_tree_map(fixture_path)
        self.assertEqual(tree_map['chr3'].start, 134196546)
        self.assertEqual(tree_map['chr3'].end, 134204866)
        self.assertEqual(tree_map['chr3'].left_node.start, 38589553)
        self.assertEqual(tree_map['chr3'].left_node.end, 38691164)

    def test_buildtreemap_root_has_right_node(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        fixture_path = "../../fixtures/gtf/hg19_fixture3.gtf"
        fixture_path = os.path.join(dir_path, fixture_path)
        tree_map = annotate.build_tree_map(fixture_path)
        self.assertEqual(tree_map['chr3'].start, 38589553)
        self.assertEqual(tree_map['chr3'].end, 38691164)
        self.assertEqual(tree_map['chr3'].right_node.start, 134196546)
        self.assertEqual(tree_map['chr3'].right_node.end, 134204866)