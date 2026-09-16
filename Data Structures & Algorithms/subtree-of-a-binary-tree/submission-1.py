# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False
        
        def dfs(root, subRoot):
            if not root:
                return False

            if isSameTree(root, subRoot):
                return True
                
            
            left = dfs(root.left, subRoot)
            right = dfs(root.right, subRoot)

            return left or right


            

            
        def isSameTree(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            return (isSameTree(p.left, q.left) and isSameTree(p.right, q.right))
        
        return dfs(root, subRoot)

            
            
            