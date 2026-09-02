"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new = {}

        def dfs(cur):
            if cur in old_to_new:
                return old_to_new[cur]
            
            #it is a new one
            clone = Node(cur.val)
            old_to_new[cur] = clone

            for nb in cur.neighbors:
                clone.neighbors.append(dfs(nb))

            return clone

        
        return dfs(node)


