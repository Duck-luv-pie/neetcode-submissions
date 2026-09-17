from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        rows = len(grid)
        cols = len(grid[0])


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col))

        while q:
            row, col = q.popleft()

            directions = [(1, 0),(-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
            
                if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[row][col] + 1
                    q.append((nr,nc))
        

