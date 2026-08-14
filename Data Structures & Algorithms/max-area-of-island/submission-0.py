class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        num_rows = len(grid)
        num_cols = len(grid[0])

        #basically use dfs to count the land area for each island 
        def dfs(row, col):
            if row < 0 or row >= num_rows or col < 0 or col >= num_cols:
                return 0
            
            if grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            
            area = 1

            area += dfs(row + 1, col)
            area += dfs(row - 1, col)
            area += dfs(row, col + 1)
            area += dfs(row, col - 1)

            return area
        #go through all possible to find each island

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    cur_area = 0
                    cur_area += dfs(row, col)
                    max_area = max(max_area, cur_area)


        return max_area


