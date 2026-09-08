# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
            #this is to stop it once the length of the BST expires
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root