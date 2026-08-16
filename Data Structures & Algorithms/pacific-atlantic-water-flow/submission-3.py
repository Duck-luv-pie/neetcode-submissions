class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        num_rows = len(heights)
        num_cols = len(heights[0])
        pacific = set()
        atlantic = set()

        res = []


        #basically starting from the oceans we want to see if we can reach any given cell. if a cell in both ocean's set add it to the list and return

        def dfs(s, row, col, prev):
            #basically check if alr in, else add to s
            if (row, col) in s:
                return 
            if not (0 <= row < num_rows) or not (0 <= col < num_cols):
                return
            
            #now that everything is in heights:
            if heights[row][col] < prev:
                return
            if (row, col) not in s and heights[row][col] >= prev:
                s.add((row, col))
            
            dfs(s, row + 1, col, heights[row][col])
            dfs(s, row - 1, col, heights[row][col])
            dfs(s, row, col + 1, heights[row][col])
            dfs(s, row, col - 1, heights[row][col])

            


        
        #go over pacific (top and left)
        #top first
        for col in range(num_cols):
            dfs(pacific, 0, col, 0)
        
        for row in range(num_rows):
            dfs(pacific, row, 0, 0)
        

        #go over atlantic (bottom and right)
        for col in range(num_cols):
            dfs(atlantic, num_rows - 1, col, 0)
        
        for row in range(num_rows):
            dfs(atlantic, row, num_cols - 1, 0)
        

        for row, col in pacific:
            if (row, col) in atlantic:
                res.append([row, col])

        return res

    