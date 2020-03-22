import unittest
from binary_tree import TreeNode, BinaryTree


class BinaryTreeTest(unittest.TestCase):
    def setUp(self):
        self.root = TreeNode(1)
        for val in [2, 3, 4, 5, 6]:
            self.root.insert(val)

    def test_insert_into_node(self):
        root = TreeNode(2)
        root.insert(1)
        root.insert(3)

        self.assertEqual(root.left, TreeNode(1))
        self.assertEqual(root.right, TreeNode(3))

    def test_deep_insert_into_node(self):
        self.assertEqual(self.root.left.left, TreeNode(4))
        self.assertEqual(self.root.left.right, TreeNode(5))

        self.assertEqual(self.root.right.left, TreeNode(6))
        self.assertEqual(self.root.right.right, None)

    def test_inorder_iteration(self):
        expected = [4, 2, 5, 1, 6, 3]
        actual = [x for x in self.root.inorder()]
        self.assertEqual(expected, actual)

    def test_tree_inorder_iteration(self):
        binary_tree = BinaryTree(self.root)
        expected = [4, 2, 5, 1, 6, 3]
        actual = [x for x in binary_tree.inorder()]
        self.assertEqual(len(binary_tree), len(expected))
        self.assertEqual(expected, actual)

    def test_tree_inorder_iteration(self):
        binary_tree = BinaryTree()
        expected = []
        actual = [x for x in binary_tree.inorder()]
        self.assertEqual(len(binary_tree), len(expected))
        self.assertEqual(expected, actual)

    def test_preorder_iteration(self):
        expected = [1, 2, 4, 5, 3, 6]
        actual = [x for x in self.root.preorder()]
        self.assertEqual(expected, actual)

    def test_postorder_iteration(self):
        expected = [4, 5, 2, 6, 3, 1]
        actual = [x for x in self.root.postorder()]
        self.assertEqual(expected, actual)

    def test_levelorder_iteration(self):
        expected = [1, 2, 3, 4, 5, 6]
        actual = [x for x in self.root.levelorder()]
        self.assertEqual(expected, actual)