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
            return

        copies = {}
        
        def dfs(original):
            if original in copies:
                return copies[original]
            
            copy = Node(original.val)

            copies[original] = copy

            for neighbour in original.neighbors:
                copy.neighbors.append(dfs(neighbour))
        
            return copy
        
        return dfs(node)

