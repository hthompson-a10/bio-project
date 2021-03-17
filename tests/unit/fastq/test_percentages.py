import unittest
from unittest.mock import patch, mock_open

from bio.fastq import percentages

SEQ_AT_30 = "B" * 30
SEQ_OVER_30 = "A" * 31
NEW_LINE_SPACER = '\n' * 4


class TestFastqPercentage(unittest.TestCase):

    def _format_filedata(self, lines):
        lines = NEW_LINE_SPACER.join(tuple(lines))
        return f"\n{lines}\n"

    def test_buildpercentagemap_0_percent_over_30(self):
        mock_lines = [SEQ_AT_30 for i in range(0, 10)]
        mock_lines = self._format_filedata(mock_lines)

        with patch("builtins.open", mock_open(read_data=mock_lines)):
            result = percentages.build_percentage_map(['mock_file_path'])
        self.assertEqual(result.get('mock_file_path'), 0)

    def test_buildpercentagemap_50_percent_over_30(self):
        mock_lines = [SEQ_AT_30 for i in range(0, 10)]
        mock_lines.extend([SEQ_OVER_30 for i in range(0, 10)])
        mock_lines = self._format_filedata(mock_lines)

        with patch("builtins.open", mock_open(read_data=mock_lines)):
            result = percentages.build_percentage_map(['mock_file_path'])
        self.assertEqual(result.get('mock_file_path'), 50)

    def test_buildpercentagemap_100_percent_over_30(self):
        mock_lines = [SEQ_OVER_30 for i in range(0, 10)]
        mock_lines = self._format_filedata(mock_lines)

        with patch("builtins.open", mock_open(read_data=mock_lines)):
            result = percentages.build_percentage_map(['mock_file_path'])
        self.assertEqual(result.get('mock_file_path'), 100)
