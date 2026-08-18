class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        count = 0

        #basically want to do dfs to turn an island to 0 while counting it.

        def dfs(row, col):
            if not (0 <= row < num_rows) or not (0 <= col < num_cols):
                return
            
            if grid[row][col] == "0":
                return
            
            grid[row][col] = "0" #change the "1" to a "0"

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        
        #now we want to go through grid and count
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row, col)
        
        return count
