# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0):
#         self.val = val
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        # keeping track of the prev, first, and second misplaced nodes
        self.prev = None
        self.first = None
        self.second = None

        # inorder traversal
        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node

            self.prev = node

            inorder(node.right)

        inorder(root)

        # swap their values to recover the bst
        self.first.val, self.second.val = self.second.val, self.first.val