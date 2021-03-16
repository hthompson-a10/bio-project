from bio.annotate import nodes
import unittest


class TestGeneNode(unittest.TestCase):

    def setUp(self):
        self.node1 = nodes.GeneBlock(1, "test_gene_1")
        self.node2 = nodes.GeneBlock(1, "test_gene_2")

    def test_eq_true(self):
        result = self.node1 == self.node2
        self.assertTrue(result)
    
    def test_ne_true(self):
        self.node1.start = 2
        result = self.node1 != self.node2
        self.assertTrue(result)
    
    def test_lt_true(self):
        self.node1.start = 0
        result = self.node1 < self.node2
        self.assertTrue(result)

    def test_gt_true(self):
        self.node1.start = 2
        result = self.node1 > self.node2
        self.assertTrue(result)

    def test_le_less_true(self):
        self.node1.start = 0
        result = self.node1 <= self.node2
        self.assertTrue(result)
    
    def test_le_equal_true(self):
        result = self.node1 <= self.node2
        self.assertTrue(result)

    def test_ge_greater_true(self):
        self.node1.start = 3
        result = self.node1 >= self.node2
        self.assertTrue(result)

    def test_ge_equal_true(self):
        result = self.node1 >= self.node2
        self.assertTrue(result)