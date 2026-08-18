class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        max_area = 0

        #dfs to get the max length of a island


        def dfs(row, col):
            #get the max maxAreaOfIsland
            if not (0 <= row < num_rows) or not (0 <= col < num_cols):
                return 0
            
            if grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0 

            return (1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1))
        
        #go over the island to see what area we can get.

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 1:
                    cur_count = 1
                    max_area = max(max_area, dfs(row, col))

        return max_area