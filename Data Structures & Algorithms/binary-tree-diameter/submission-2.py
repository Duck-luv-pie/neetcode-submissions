# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def depth(node):
            if not node:
                return 0
            #we want to find the max of the left and the right, and combine for cur

            nonlocal max_diameter

            left = depth(node.left)
            right = depth(node.right)

            cur_diameter = left + right
            max_diameter = max(max_diameter, cur_diameter)

            return 1 + max(left, right)
        
        depth(root)
        return max_diameter