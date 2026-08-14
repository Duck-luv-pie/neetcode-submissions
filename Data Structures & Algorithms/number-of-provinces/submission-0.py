class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()

        number_of_nodes = len(isConnected)
        provinces = 0

        #dfs to check neighbours:
        def dfs(node):
            visited.add(node)
            for neighbour in range(number_of_nodes):
                if isConnected[node][neighbour] == 1 and neighbour not in visited:
                    dfs(neighbour)

        #go through and see if visited if not we can add provinces

        for node in range(number_of_nodes):
            if node not in visited:
                provinces += 1
                dfs(node)
        
        return provinces

