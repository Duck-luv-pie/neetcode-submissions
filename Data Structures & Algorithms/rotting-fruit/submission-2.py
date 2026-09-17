from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        minutes = 0
        q = deque()

        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    q.append((row, col))
        
        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for dr,dc in directions:
                    nr = row + dr
                    nc = col + dc

                    if (0 <= nr < rows) and (0 <= nc < cols) and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr,nc))
            minutes += 1
        if fresh > 0:
            return -1
        
        return minutes


            