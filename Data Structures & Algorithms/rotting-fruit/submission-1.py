from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        minutes = 0 

        rows = len(grid)
        cols = len(grid[0])

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1
        
        #dfs time

        while queue and fresh > 0:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change

                    if (0 <= new_row < rows) and (0 <= new_col < cols):
                        if grid[new_row][new_col] == 1:
                            grid[new_row][new_col] = 2
                            queue.append((new_row, new_col))
                            fresh -= 1
            
            minutes += 1

        if fresh > 0:
            return -1 
        
        return minutes
                            

            