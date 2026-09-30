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

            found = dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1)
        
            board[r][c] = tmp

            return found
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        
        return False