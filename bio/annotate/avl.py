import copy
import nodes

class TreeDoesNotContainNodeError(Exception):
    pass


class GeneTreeNode(nodes.GeneBlock):

    def __init__(self, start, gene_name):
        self.left_node = None
        self.right_node = None
        self.height = 1
        super().__init__(start, gene_name)


class AVLGeneTree(object):

    def _get_child_heights(self, node):
        left_height = node.left_node.height if node.left_node else 0
        right_height = node.right_node.height if node.right_node else 0
        return left_height, right_height

    def _calc_balance(self, node): 
        left_height, right_height = self._get_child_heights(node)
        return left_height - right_height

    def _calc_height(self, node):
        left_height, right_height = self._get_child_heights(node)
        return 1 + max(left_height, right_height)

    def _merge(self, root, node):
        for i in range(len(root.annotations), len(node.annotations)):
            root.annotations.append(node.annotations[i])
        root.end = root.annotations[-1].end
        return root

    def insert(self, root, node):
        if not root:
            return node
        elif node.start < root.start:
            root.left_node = self.insert(root.left_node, node)
        elif node.start > root.start:
            root.right_node = self.insert(root.right_node, node)
        else:
            if len(root.annotations) < len(node.annotations):
                root = self._merge(root, node)
            return root

        root.height = self._calc_height(root)
        balance_factor = self._calc_balance(root)

        # Check if left side causing the tree to be unbalaced
        if balance_factor > 1:
            if node.start < root.left_node.start:
                # If node was inserted as a left leaf then rotate right to compensate
                return self.rotate_right(root)
            else:
                # If node was inserted as a right leaf then make the node the new parent
                # of the root's left subtree. Then, perform a right rotation compensate
                # for the left side being unbalanced
                root.left_node = self.rotate_left(root.left_node)
                return self.rotate_right(root)

        # Check if right side causing the tree to be unbalaced
        if balance_factor < -1:
            if node.start > root.right_node.start:
                # If node was inserted as a right leaf then rotate left to compensate
                return self.rotate_left(root)
            else:
                # If node was inserted as a left leaf then make the node the new parent
                # of the root's right subtree. Then, perform a left rotation compensate
                # for the right side being unbalanced
                root.right_node = self.rotate_right(root.right_node)
                return self.rotate_left(root)
        return root

    def rotate_left(self, node):
        new_parent = node.right_node
        left_subtree = new_parent.left_node

        new_parent.left_node = node
        node.right_node = left_subtree

        node.height = self._calc_height(node)
        new_parent.height = self._calc_height(new_parent)

        return new_parent

    def rotate_right(self, node):
        new_parent = node.left_node
        right_subtree = new_parent.right_node

        new_parent.right_node = node
        node.left_node = right_subtree

        node.height = self._calc_height(node)
        new_parent.height = self._calc_height(new_parent)

        return new_parent

    def search(self, node, coordinate):
        """
        This searches across the AVL tree and annotation nodes to find the annotation
        connected to the provided coordinate.
        """
        if node is None:
            import pdb; pdb.set_trace()
            raise TreeDoesNotContainNodeError()
        
        if coordinate < node.start:
            return self.search(node.left_node, coordinate)

        if coordinate >= node.start:
            if coordinate <= node.end:
                return node
            else:
                return self.search(node.right_node, coordinate)

    def in_order(self, root):
        if not root:
            return
        self.in_order(root.left_node)
        print("{0} ".format(root.start), end="")
        self.in_order(root.right_node)