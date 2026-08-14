class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        num_islands = 0

        def dfs(row, column):
            if row < 0 or row >= num_rows or column < 0 or column >= num_cols:
                return
            
            if grid[row][column] != "1":
                return
            
            grid[row][column] = "0"

            dfs(row + 1, column)
            dfs(row -1, column)
            dfs(row, column + 1)
            dfs(row, column - 1)
        
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == "1":
                    num_islands += 1
                    dfs(row, col)
        
        return num_islands

            

