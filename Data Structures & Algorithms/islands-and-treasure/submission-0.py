from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col))
        
        while q:
            r, c = q.popleft()
            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647):
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))
        

