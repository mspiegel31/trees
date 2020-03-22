from collections import deque
from typing import Any, Type


class TreeNode:
    def __init__(self, val: Any = None, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return 'TreeNode(val={}, left={}, right={}, parent={})'.format(self.val, self.left, self.right, self.parent)

    def __str__(self):
        return str(self.val)

    def __eq__(self, other):
        if other == None:
            return False
        val_match = self.val == other.val
        pointer_match = self.left == other.left and self.right == other.right

        return val_match and pointer_match

    def is_left(self):
        return self.parent.left == self

    def is_right(self):
        return self.parent.right == self

    def insert(self, val: Any):
        """
        insert new data by level order below this node

        Example:
        node = TreeNode(1)
        for i in range(2, 7):
            node.insert(i)

        yields the tree:
             1
           /   \
          2     3
         / \   /
        4   5 6
        """
        queue = deque([self])

        while queue:
            node = queue.popleft()

            if node:
                if node.left == None:
                    node.left = TreeNode(val, parent=node)
                    return
                if node.right == None:
                    node.right = TreeNode(val, parent=node)
                    return
                queue.append(node.left)
                queue.append(node.right)

    def inorder(self):
        """
        traverse this node and all children in order (left, root, right)
        """
        node = self
        stack = []
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node.val
                node = node.right

    def preorder(self):
        """
        traverse this node and all children in preorder (root, left, right)
        """
        stack = [self]
        while stack:
            node = stack.pop()
            if node:
                yield node.val
                stack.append(node.right)
                stack.append(node.left)

    def postorder(self):
        """
        traverse this node and all children in postorder (left, right, root)
        """
        node = self
        last_node_visited = None
        stack = []
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                peek = stack[len(stack) - 1]
                if peek.right and last_node_visited != peek.right:
                    node = peek.right
                else:
                    yield peek.val
                    last_node_visited = stack.pop()
                    node = None
    
    def levelorder(self):
        """
        traverse this node and all children by level
        """
        queue = deque([self])

        while queue:
            node = queue.popleft()

            if node:
                yield node.val
                queue.append(node.left)
                queue.append(node.right)


class BinaryTree:
    def __init__(self, root: TreeNode = None):
        self.length = 0
        self.root = root
        if root != None:
            for node in root.inorder():
                self.length += 1

    def __len__(self):
        return self.length

    def __repr__(self):
        return self.root.__repr__()

    def __str__(self):
        return self.root.__str__()

    def _check_empty(self):
        if self.root == None:
            raise IndexError('Tree is Empty')

    def insert(self, val: Any):
        if self.root == None:
            self.root = TreeNode(val)
        else:
            self.root.insert(val)

        self.length += 1

    def remove(self, val):
        if self.root == None:
            raise IndexError('Tree is Empty')
        else:
            self.root.remove(val)

        self.length -= 1

    def inorder(self):
        if self.root == None:
            return
        for val in self.root.inorder():
            yield val
