from collections import deque
from typing import Any, Type


class TreeNode:
    def __init__(self, val: Any=None, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return 'TreeNode(val={}, left={}, right={})'.format(self.val, self.left, self.right)
    
    def insert(self, val: Any):
        """
        insert new data into a node by level order into any ndoes below this node
        """
        queue = deque([self])

class BinaryTree:
    def __init__(self, root: TreeNode=None):
        self.length = 0
        self.root = root
    
    def insert(self, val: Any):
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self.root.insert(val)


