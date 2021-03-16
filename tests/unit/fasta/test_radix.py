import unittest
from unittest import mock
from unittest.mock import patch

from bio.fasta import radix


class TestRadixSort(unittest.TestCase):

    def test_countingsort_empty_no_failure(self):
        actual_list = []
        radix.RadixSort()._counting_sort(actual_list, 1)
        self.assertEqual(actual_list, [])

    def test_countingsort_reverse_order(self):
        mock_1 = mock.Mock(cnt=1)
        mock_2 = mock.Mock(cnt=2)
        mock_3 = mock.Mock(cnt=3)
        actual_list = [mock_3, mock_2, mock_1]
        expected_list = [mock_1, mock_2, mock_3]
        radix.RadixSort()._counting_sort(actual_list, 1)
        self.assertEqual(actual_list, expected_list)

    def test_countingsort_in_order(self):
        mock_1 = mock.Mock(cnt=1)
        mock_2 = mock.Mock(cnt=2)
        mock_3 = mock.Mock(cnt=3)
        actual_list = [mock_1, mock_2, mock_3]
        expected_list = [mock_1, mock_2, mock_3]
        radix.RadixSort()._counting_sort(actual_list, 1)
        self.assertEqual(actual_list, expected_list)

    def test_countingsort_scrambled(self):
        mock_1 = mock.Mock(cnt=1)
        mock_2 = mock.Mock(cnt=2)
        mock_3 = mock.Mock(cnt=3)
        actual_list = [mock_1, mock_3, mock_2]
        expected_list = [mock_1, mock_2, mock_3]
        radix.RadixSort()._counting_sort(actual_list, 1)
        self.assertEqual(actual_list, expected_list)

    def test_sort_max_is_ones(self):
        with patch.object(radix.RadixSort, '_counting_sort') as mock_sort:
            radix.RadixSort().sort([], 1)
        self.assertEqual(mock_sort.call_count, 1)

    def test_sort_max_is_tens(self):
        with patch.object(radix.RadixSort, '_counting_sort') as mock_sort:
            radix.RadixSort().sort([], 10)
        self.assertEqual(mock_sort.call_count, 2)

    def test_sort_max_is_hundreds(self):
        with patch.object(radix.RadixSort, '_counting_sort') as mock_sort:
            radix.RadixSort().sort([], 100)
        self.assertEqual(mock_sort.call_count, 3)

    def test_sort_max_is_thousands(self):
        with patch.object(radix.RadixSort, '_counting_sort') as mock_sort:
            radix.RadixSort().sort([], 1000)
        self.assertEqual(mock_sort.call_count, 4)
