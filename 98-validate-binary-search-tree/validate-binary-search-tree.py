# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # helper function to validate the bst
        def validate(node, low, high):
            if not node:
                return True

            # check if the curr node is within the valid range
            if node.val <= low or node.val >= high:
                return False

            # validate the left and right subtrees
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))

        return validate(root, float("-inf"), float("inf"))