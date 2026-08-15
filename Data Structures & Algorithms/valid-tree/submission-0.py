from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n -1:
            return False
            
        graph = [[] for _ in range(n)]

        for left, right in edges:
            graph[left].append(right)
            graph[right].append(left)

        queue = deque([0])
        visited = {0}

        while queue:
            node = queue.popleft()

            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        
        return len(visited) == n

                    
                

        
