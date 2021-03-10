from bio_project.bio.fasta import nodes
import unittest


class TestSeqNode(unittest.TestCase):

    def setUp(self):
        self.node1 = nodes.SeqNode("test1", "test")
        self.node2 = nodes.SeqNode("test2", "test")

    def test_eq_true(self):
        result = self.node1 == self.node2
        self.assertTrue(result)
    
    def test_ne_true(self):
        self.node1.cnt = 2
        result = self.node1 != self.node2
        self.assertTrue(result)
    
    def test_lt_true(self):
        self.node1.cnt = 0
        result = self.node1 < self.node2
        self.assertTrue(result)

    def test_gt_true(self):
        self.node1.cnt = 2
        result = self.node1 > self.node2
        self.assertTrue(result)

    def test_le_less_true(self):
        self.node1.cnt = 0
        result = self.node1 <= self.node2
        self.assertTrue(result)
    
    def test_le_equal_true(self):
        result = self.node1 <= self.node2
        self.assertTrue(result)

    def test_ge_greater_true(self):
        self.node1.cnt = 3
        result = self.node1 >= self.node2
        self.assertTrue(result)

    def test_ge_equal_true(self):
        result = self.node1 >= self.node2
        self.assertTrue(result)


class TestFastaFrequency(unittest.TestCase):
    
    def 