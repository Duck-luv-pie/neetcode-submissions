"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def dfs(cur):
            if not cur:
                return
            
            if cur in old_to_new:
                return old_to_new[cur]
            
            #now we know for sure that it isn't in old_to_new

            copy = Node(cur.val)
            old_to_new[cur] = copy

            #now that we put it in we got to add the neighbors
            for neighbor in cur.neighbors:
                copy.neighbors.append(dfs(neighbor))

            #return the copy since we didn't do that yet
            return copy
        
        return dfs(node)







