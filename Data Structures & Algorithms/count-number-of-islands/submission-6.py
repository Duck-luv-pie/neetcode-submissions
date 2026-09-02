class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0 

        #define dfs up top
        def dfs(row, col):
            #we will use this to get rid of the current island
            if (not (0 <= row < rows)) or (not (0 <= col < cols)):
                return
            
            if grid[row][col] == "0":
                return
            
            #now we know grid is "1"
            grid[row][col] = "0"

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)


        #we need to go through each instance and do dfs on it
        #we want to count first before we destroy the island

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row, col)

        return count