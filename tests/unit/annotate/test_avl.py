import unittest
from unittest import mock

from bio.annotate import avl


class TestAVLTree(unittest.TestCase):

    def test_get_child_heights(self):
        mock_node = mock.Mock()
        mock_node.left_node.height = 2
        mock_node.right_node.height = 3
        lh, rh = avl.AVLGeneTree()._get_child_heights(mock_node)
        self.assertEqual(lh, 2)
        self.assertEqual(rh, 3)

    @mock.patch.object(avl.AVLGeneTree, '_get_child_heights', return_value=(1,2))
    def test_calc_balance(self, mock_height):
        mock_height.return_value = (1, 2)
        result = avl.AVLGeneTree()._calc_balance(mock.Mock())
        self.assertEqual(result, -1)

    @mock.patch.object(avl.AVLGeneTree, '_get_child_heights', return_value=(1,2))
    def test_calc_height(self, mock_height):
        mock_height.return_value = (1, 2)
        result = avl.AVLGeneTree()._calc_height(mock.Mock())
        self.assertEqual(result, 3)

    def test_merge(self):
        gen_anno = lambda x : [mock.Mock() for i in range(0, x)]
        mock_root = mock.Mock(annotations=gen_anno(2))
        mock_node = mock.Mock(annotations=gen_anno(5))
        mock_root = avl.AVLGeneTree()._merge(mock_root, mock_node)
        self.assertEqual(len(mock_root.annotations), 5)

    def test_insert_empty_root(self):
        mock_root = None
        mock_node = mock.Mock()
        mock_root = avl.AVLGeneTree().insert(mock_root, mock_node)
        self.assertEqual(mock_root, mock_node)

    @mock.patch.object(avl.AVLGeneTree, '_calc_balance', return_value=0)
    @mock.patch.object(avl.AVLGeneTree, '_calc_height', return_value=0)
    def test_insert_left_insert_called(self, mock_height, mock_balance):
        mock_root = mock.Mock(start=10)
        mock_root.left_node = None
        mock_node = mock.Mock(start=0)
        mock_root = avl.AVLGeneTree().insert(mock_root, mock_node)
        self.assertEqual(mock_root.left_node, mock_node)

    @mock.patch.object(avl.AVLGeneTree, '_calc_balance', return_value=0)
    @mock.patch.object(avl.AVLGeneTree, '_calc_height', return_value=0)
    def test_insert_right_insert_called(self, mock_height, mock_balance):
        mock_root = mock.Mock(start=10)
        mock_root.right_node = None
        mock_node = mock.Mock(start=20)
        mock_root = avl.AVLGeneTree().insert(mock_root, mock_node)
        self.assertEqual(mock_root.right_node, mock_node)

    @mock.patch.object(avl.AVLGeneTree, '_calc_balance', return_value=0)
    @mock.patch.object(avl.AVLGeneTree, '_calc_height', return_value=0)
    @mock.patch.object(avl.AVLGeneTree, '_merge')
    def test_insert_merge_called(self, mock_merge, mock_height, mock_balance):
        mock_root = mock.Mock(start=10, annotations=[mock.Mock()])
        mock_node = mock.Mock(start=10, annotations=[mock.Mock(), mock.Mock()])
        mock_root = avl.AVLGeneTree().insert(mock_root, mock_node)
        mock_merge.assert_called_once()

    @mock.patch.object(avl.AVLGeneTree, '_calc_height', return_value=0)
    @mock.patch.object(avl.AVLGeneTree, 'rotate_right')
    @mock.patch.object(avl.AVLGeneTree, 'rotate_left')
    def test_insert_ll_right_rotate_called(self, mock_rotate_left, mock_rotate_right, mock_height):
        mock_root = mock.Mock(start=10)
        mock_root.left_node = mock.Mock(start=5, left_node=None)
        mock_rotate_right.return_value = mock_root.left_node
        mock_node = mock.Mock(start=0)

        avl.AVLGeneTree._calc_balance = lambda y,x : 2 if x == mock_root else 0
        avl.AVLGeneTree().insert(mock_root, mock_node)

        mock_rotate_right.assert_called_with(mock_root)
        mock_rotate_left.assert_not_called()

    @mock.patch.object(avl.AVLGeneTree, '_calc_height', return_value=0)
    @mock.patch.object(avl.AVLGeneTree, 'rotate_right')
    @mock.patch.object(avl.AVLGeneTree, 'rotate_left')
    def test_insert_rr_left_rotate_called(self, mock_rotate_left, mock_rotate_right, mock_height):
        mock_root = mock.Mock(start=5)
        mock_root.right_node = mock.Mock(start=10, right_node=None)
        mock_rotate_left.return_value = mock_root.right_node
        mock_node = mock.Mock(start=15)

        avl.AVLGeneTree._calc_balance = lambda y,x : -2 if x == mock_root else 0
        avl.AVLGeneTree().insert(mock_root, mock_node)

        mock_rotate_left.assert_called_with(mock_root)
        mock_rotate_right.assert_not_called()

    @mock.patch.object(avl.AVLGeneTree, '_calc_height', return_value=0)
    @mock.patch.object(avl.AVLGeneTree, 'rotate_right')
    @mock.patch.object(avl.AVLGeneTree, 'rotate_left')
    def test_insert_lr_left_right_called(self, mock_rotate_left, mock_rotate_right, mock_height):
        mock_root = mock.Mock(start=10)
        mock_root.left_node = mock.Mock(start=5, right_node=None)
        mock_rotate_right.return_value = mock_root.left_node
        mock_node = mock.Mock(start=7)

        avl.AVLGeneTree._calc_balance = lambda y,x : 2 if x == mock_root else 0
        avl.AVLGeneTree().insert(mock_root, mock_node)

        mock_rotate_left.assert_called()
        mock_rotate_right.assert_called_with(mock_root)

    @mock.patch.object(avl.AVLGeneTree, '_calc_height', return_value=0)
    @mock.patch.object(avl.AVLGeneTree, 'rotate_right')
    @mock.patch.object(avl.AVLGeneTree, 'rotate_left')
    def test_insert_rl_right_left_called(self, mock_rotate_left, mock_rotate_right, mock_height):
        mock_root = mock.Mock(start=5)
        mock_root.right_node = mock.Mock(start=10, left_node=None)
        mock_rotate_left.return_value = mock_root.right_node
        mock_node = mock.Mock(start=7)

        avl.AVLGeneTree._calc_balance = lambda y,x : -2 if x == mock_root else 0
        avl.AVLGeneTree().insert(mock_root, mock_node)

        mock_rotate_right.assert_called()
        mock_rotate_left.assert_called_with(mock_root)

    def test_search_node_unkown(self):
        result = avl.AVLGeneTree().search(None, 0)
        self.assertEqual(result.gene_name, 'UNKNOWN')

    def test_search_coordinate_less_than_root(self):
        mock_left = mock.Mock(start=0, end=1, gene_name="SUCCESS")
        mock_right = mock.Mock(start=4, end=5, gene_name="FAILED")
        mock_node = mock.Mock(start=2, end=3, left_node=mock_left, right_node=mock_right)
        result = avl.AVLGeneTree().search(mock_node, 0)
        self.assertEqual(result.gene_name, 'SUCCESS')

    def test_search_coordinate_greater_than_root(self):
        mock_left = mock.Mock(start=0, end=1, gene_name="FAILED")
        mock_right = mock.Mock(start=4, end=5, gene_name="SUCCESS")
        mock_node = mock.Mock(start=2, end=3, left_node=mock_left, right_node=mock_right)
        result = avl.AVLGeneTree().search(mock_node, 4)
        self.assertEqual(result.gene_name, 'SUCCESS')