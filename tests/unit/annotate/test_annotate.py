import copy
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
        annotate._create_annotation_node = lambda x : anno_1 if x == 'line1\n' else anno_2
        mock_lines = self._format_filedata(['line1', 'line2'])
        with mock.patch("builtins.open", mock_open(read_data=mock_lines)) as mock_file:
            result = annotate.build_tree_map(['mock_file_path'])
        self.assertEqual(len(result.keys()), 1)


    @mock.patch.object(avl.AVLGeneTree, 'insert')
    def test_buildtreemap_no_duplicate_chromosomes(self, mock_tree):
        anno_1 = mock.Mock(gene_name='mock_gene', chromosome='chr1')
        anno_2 = mock.Mock(gene_name='mock_gene2', chromosome='chr2')
        annotate._create_annotation_node = lambda x : anno_1 if x == 'line1\n' else anno_2
        mock_lines = self._format_filedata(['line1', 'line2'])
        with mock.patch("builtins.open", mock_open(read_data=mock_lines)) as mock_file:
            result = annotate.build_tree_map(['mock_file_path'])
        self.assertEqual(len(result.keys()), 2)