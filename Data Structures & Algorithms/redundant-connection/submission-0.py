class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB: #they are in the same tree before this connection. this connectino would result in a cycle
                return False
            
            parent[rootB] = rootA

            return True
        

        for a, b in edges:
            if not union(a, b):
                return [a, b]

