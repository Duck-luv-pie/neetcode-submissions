class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True

            if not (0 <= r < rows) or not (0 <= c < cols):
                return False
            
            if board[r][c] != word[i]:
                return False
            
            tmp = board[r][c]
            board[r][c] = "#"

            found = (dfs(r + 1, c, i + 1) or dfs(r -1, c, i + 1) or dfs(r, c+1, i +1) or dfs(r, c-1, i + 1))

            board[r][c] = tmp
            
            return found
        


        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0) == True:
                        return True
        
        return False
