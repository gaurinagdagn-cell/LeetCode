# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #inorder traversal = left->root->right

        ans = []

        #helper func for recursive inorder traversal
        def inorder(node):
            if not node:
                return

            # traverse the left subtree
            inorder(node.left)

            #visit the current node
            ans.append(node.val)

            # traverse the right subtree
            inorder(node.right)

        inorder(root)

        return ans
        