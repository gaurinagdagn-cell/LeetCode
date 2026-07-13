# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both nodes are none
        if not p and not q:
            return True

        # one is none or values are different
        if not p or not q or p.val != q.val:
            return False

        # recursively compare the left and right subtrees
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))