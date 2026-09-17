from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #go through the root tree and see if it is same tree or not

        if not subRoot:
            return True
        
        if not root:
            return False
        


        def isSameTree(p, q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False
            
            if p.val != q.val:
                return False
            
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        
        q = deque([root])

        while q:
            node = q.popleft()
            if isSameTree(node, subRoot):
                return True
            
            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)
            
            

        return False
 