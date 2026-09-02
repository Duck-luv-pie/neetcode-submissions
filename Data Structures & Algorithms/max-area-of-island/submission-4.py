class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0


        #we need a dfs function to find the area of a given island
        def dfs(row, col):
            if (not (0 <= row < rows)) or (not (0 <= col < cols)):
                return 0
            
            if grid[row][col] == 0:
                return 0
            
            #now we know it is 1, so add 1
            grid[row][col] = 0
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)

        #go through the matrix to find islands and record the biggest one
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))
        
        return max_area