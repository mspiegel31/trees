import unittest
from binary_tree import TreeNode

class BinaryTreeTest(unittest.TestCase):
    
    def test_insert_into_node(self):
        root = TreeNode(2)
        root.insert(1)
        root.insert(3)
        
        self.assertEqual(root.left, TreeNode(1))
        self.assertEqual(root.left, TreeNode(3))