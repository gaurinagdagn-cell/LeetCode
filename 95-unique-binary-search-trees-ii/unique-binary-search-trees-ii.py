# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # helper function 
        def build(start, end):
            if start > end:
                return [None]

            trees = []

            for root in range(start, end + 1):
                # all possible left subtrees
                left_trees = build(start, root - 1)

                #  all possible right subtrees
                right_trees = build(root + 1, end)

                # combining every left and right subtree with the current root
                for left in left_trees:
                    for right in right_trees:
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees.append(node)

            return trees

        return build(1, n)