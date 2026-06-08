class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]

        for r in range(len(rows)):
            for c in range(len(cols)):
                val = board[r][c]

                if val == '.':
                    continue
            
                grid_idx = (r//3) * 3 + (c//3)

                if val in rows[r] or val in cols[c] or val in grids[grid_idx]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                grids[grid_idx].add(val)
        return True
        
