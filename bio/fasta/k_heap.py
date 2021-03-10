import copy
import math

class KHeap(object):

    """
        This is a partial implementation of the K-ary Heap which is the generalized version of the
        binary heap (k=2).

        This was only partially implemented as anything more would have been out-of-scope of this assignment.
        In a normal codebase, the author would have implemented the entirety of the class.

        For readability purposes: Let k be aliased to child_cnt

        Credit to https://www.geeksforgeeks.org/k-ary-heap/ for the base implementation in C++
    """

    def _swap(self, node_list, idx_1, idx_2):
        temp_node = copy.deepcopy(node_list[idx_1])
        node_list[idx_1] = copy.deepcopy(node_list[idx_2])
        node_list[idx_2] = temp_node

    def build_heap(self, node_list, size, child_cnt):
        i = math.floor((size-1)/child_cnt)
        while i >= 0:
            self.max_heapify(node_list, size, i, child_cnt)
            i -= 1

    def max_heapify(self, node_list, size, idx, child_cnt):
        while True:
            child_idx_list = []
            # Find all the children of the current node
            # Children are at (child_cnt*idx)+1, ..., (child_cnt*idx)+child_cnt
            # Iterating from 1 -> child_cnt+1 makes calculations easier
            for i in range(1, child_cnt+1):
                potential_child_idx = child_cnt*idx + i
                if potential_child_idx < size:
                    child_idx_list.append(potential_child_idx)
                else:
                    child_idx_list.append(-1) # Use -1 to signify out-of-bounds child pos

            max_child = -1
            max_child_idx = -1
            # Find the largest child node
            for child_idx in child_idx_list:
                if child_idx != -1 and node_list[child_idx] > max_child:
                    max_child_idx = child_idx
                    max_child = node_list[child_idx]

            # If this is true then we are on a leafe node
            if max_child == -1:
                break

            # Swap current node with it's child if child is larger
            if (node_list[idx] < node_list[max_child_idx]):
                self._swap(node_list, idx, max_child_idx)
            
            idx = max_child_idx

    def extract_max(self, node_list, size, child_cnt):
        max_node = node_list[0]
        node_list[0] = node_list[size-1]
        del node_list[size-1]
        size -= 1

        self.max_heapify(node_list, size, 0, child_cnt)

        return max_node