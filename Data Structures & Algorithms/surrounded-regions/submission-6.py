from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        q = deque()
        #now go through the borders to add them to the queue
        for col in range(cols):
            if board[0][col] == "O":
                q.append((0, col))
            if board[rows-1][col] == "O":
                q.append((rows-1, col))
        
        for row in range(1, rows-1):
            if board[row][0] == "O":
                q.append((row, 0))
            if board[row][cols-1] == "O":
                q.append((row, cols-1))
            

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            row, col = q.popleft()
            board[row][col] = "T"
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc
            
                if (0 < nr < (rows-1)) and (0 < nc < (cols-1)):
                    if board[nr][nc] == "O":
                        board[nr][nc] = "T"
                        q.append((nr,nc))
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "T":
                    board[row][col] = "O"



            
            