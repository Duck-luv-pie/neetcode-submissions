# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maximum):
            if not node:
                return 0
            good = 1 if node.val >= maximum else 0
            maximum = max(node.val, maximum)

            return good + dfs(node.left, maximum) + dfs(node.right, maximum)
        
        return dfs(root, root.val)
        
