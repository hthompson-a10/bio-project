import unittest
from unittest import mock
from unittest.mock import patch

from bio.fasta import d_heap
from bio.fasta import nodes



class TestDHeap(unittest.TestCase):
    
    def _node_list_generator(self, n):
        node_list = []
        for i in range(0, n):
            node_list.append(nodes.SeqNode("mock_sequence"))
        return node_list

    def test_swap(self):
        mock_node_1 = mock.MagicMock()
        mock_node_2 = mock.MagicMock()
        node_list = [mock_node_1, mock_node_2]
        heap = d_heap.DHeap()

        heap._swap(node_list, 0, 1)
        self.assertEqual(node_list[0], mock_node_2)
        self.assertEqual(node_list[1], mock_node_1)

    def test_buildheap_empty_maxheapify_not_called(self):
        child_cnt = 2
        node_list = []
        with patch.object(d_heap.DHeap, 'max_heapify') as mock_heapify:
            heap = d_heap.DHeap()
            heap.build_heap(node_list, len(node_list), child_cnt)
        mock_heapify.assert_not_called()

    def test_buildheap_root_only_maxheapify_not_called(self):
        child_cnt = 2
        node_list = self._node_list_generator(1)
        with patch.object(d_heap.DHeap, 'max_heapify') as mock_heapify:
            heap = d_heap.DHeap()
            heap.build_heap(node_list, len(node_list), child_cnt)
        mock_heapify.assert_not_called()

    def test_buildheap_one_parent_maxheapify_called(self):
        child_cnt = 4
        node_list = self._node_list_generator(3)
        with patch.object(d_heap.DHeap, 'max_heapify') as mock_heapify:
            heap = d_heap.DHeap()
            heap.build_heap(node_list, len(node_list), child_cnt)
        mock_heapify.assert_called_with(node_list, len(node_list), 0, child_cnt)

    def test_buildheap_multi_parent_maxheapify_called(self):
        child_cnt = 3
        node_list = self._node_list_generator(7)
        with patch.object(d_heap.DHeap, 'max_heapify') as mock_heapify:
            heap = d_heap.DHeap()
            heap.build_heap(node_list, len(node_list), child_cnt)
        mock_heapify.assert_called_with(node_list, len(node_list), 0, child_cnt)

    def test_maxheapify_parent_is_max_swap_not_called(self):
        child_cnt = 3
        node_list = self._node_list_generator(4)
        node_list[0].cnt = 128
        with patch.object(d_heap.DHeap, '_swap') as mock_swap:
            heap = d_heap.DHeap()
            heap.max_heapify(node_list, len(node_list), 0, 3)
        mock_swap.assert_not_called()

    def test_maxheapify_child_is_max_swap_called(self):
        child_cnt = 3
        node_list = self._node_list_generator(4)
        node_list[3].cnt = 128
        with patch.object(d_heap.DHeap, '_swap') as mock_swap:
            heap = d_heap.DHeap()
            heap.max_heapify(node_list, len(node_list), 0, 3)
        mock_swap.assert_called_with(node_list, 0, 3)