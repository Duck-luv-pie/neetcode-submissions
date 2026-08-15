class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        max_area = 0

        #dfs to get rid of the island and get the max area of it
        def dfs(row, col):
            if not (0 <= row < num_rows) or not (0 <= col < num_cols):
                return 0
            
            if grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            count = 1

            return count + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)


        #go through to find the islands
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    cur_area = 0
                    cur_area += dfs(row, col)
                    max_area = max(max_area, cur_area)



        return max_area