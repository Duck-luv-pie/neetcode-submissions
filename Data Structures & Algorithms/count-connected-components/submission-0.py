class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i : [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        
        seen = set()

        def dfs(node):
            if node in seen:
                return
            
            seen.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)


            
        count = 0

        for node in range(n):
            if node not in seen:
                count += 1
                dfs(node)
        
        return count