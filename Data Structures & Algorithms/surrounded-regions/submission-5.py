class Solution:
    def solve(self, board: List[List[str]]) -> None:
        num_rows = len(board)
        num_cols = len(board[0])

        seen = set()


        def dfs(row, col): #go through and if you find a O put coords in the set
            if not (0 <= row < num_rows) or not (0 <= col < num_cols):
                return
            
            if board[row][col] == "X":
                return
            
            if (row, col) in seen:
                return
            
            #now board is equal to "O" within the region
            seen.add((row,col))
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        #basically we want to go over the edges and put every connecting region into a seen

        #go over the edges:
        for row in range(num_rows):
            for col in range(num_cols):
                if (row == 0 or row == (num_rows - 1)) or (col == 0 or col == (num_cols - 1)): #ie if it's on the edges
                    if (row,col) not in seen and board[row][col] == "O":
                        dfs(row, col)



        #besides all the seen regions turn everything to X
        for row in range(num_rows):
            for col in range(num_cols):
                if (row, col) not in seen:
                    board[row][col] = "X"