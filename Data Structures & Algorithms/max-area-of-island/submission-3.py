class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        max_area = 0

        def dfs(row, col): #we neeed to turn the found area into 0s
            if not ((0 <= row < rows) and (0 <= col < cols)):
                return 0
            
            if grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            
            return (1 + dfs(row + 1, col) + dfs(row -1, col) + dfs(row, col + 1) + dfs(row, col - 1))
        

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row, col))
        
        return max_area