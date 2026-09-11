class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        numOfIslands = 0

        def dfs(row, col): #this will turn the counted island into water
            if not (0 <= row < rows) or not (0 <= col < cols):
                return
            
            if grid[row][col] == "0":
                return
            
            grid[row][col] = "0" #because it was guaranteed to be 1

            #now do dfs on the rest of the surrounding ones till none are left

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        #now we need to go through each of the parts of the grid until no islands are left

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    numOfIslands += 1
                    dfs(row, col)
        
        return numOfIslands