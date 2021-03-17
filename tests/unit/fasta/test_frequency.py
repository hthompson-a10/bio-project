import unittest
from unittest import mock
from unittest.mock import patch, mock_open

from bio.fasta import frequency


class TestFrequency(unittest.TestCase):

    def test_convertolist_empty(self):
        test_dict = {}
        result = frequency.convert_to_list(test_dict)
        self.assertEqual(result, [])

    def test_convertolist(self):
        test_dict = {'a': 1, 'b': 2, 'c': 3}
        result = frequency.convert_to_list(test_dict)
        self.assertEqual(result, [1, 2, 3])

    @patch('bio.fasta.frequency.nodes.SeqNode')
    def test_buildsequencedict_duplicate_increase_cnt(self, mock_seq_node):
        mock_seq_node.return_value = mock.Mock(cnt=1)
        mock_lines = ('>seq1', 'test_seq',
                      '>seq2', 'test_seq')
        mock_lines = '\n'.join(mock_lines) + '\n'
        with patch("builtins.open", mock_open(read_data=mock_lines)):
            result = frequency.build_sequence_dict('mock_file_path')[0]
        self.assertEqual(result.get('test_seq').cnt, 2)

    def test_buildsequencedict_no_duplicate_increase_nodes(self):
        mock_lines = ('>seq1', 'test_seq',
                      '>seq2', 'test_seq2')
        mock_lines = '\n'.join(mock_lines)
        with patch("builtins.open", mock_open(read_data=mock_lines)):
            result = frequency.build_sequence_dict('mock_file_path')[0]
        self.assertIsNotNone(result.get('test_seq'))
        self.assertIsNotNone(result.get('test_seq2'))
