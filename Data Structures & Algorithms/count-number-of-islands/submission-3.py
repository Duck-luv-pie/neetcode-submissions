class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        num_islands = 0

        #do dfs to get rid of the island we just found
        def dfs(row, col):
            if not (0 <= row < num_rows) or not (0 <= col < num_cols):
                return
            
            if grid[row][col] == "0":
                return
            
            grid[row][col] = "0"

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        #look for numIslands
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == "1":
                    num_islands += 1
                    dfs(row, col)
        
        return num_islands
