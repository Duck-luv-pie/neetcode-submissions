class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(row: int, col: int) -> None:
            # Stop if out of bounds or not unvisited land
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or grid[row][col] != "1"
            ):
                return

            # Mark this land cell as visited
            grid[row][col] = "0"

            # Visit connected land
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)

        return islands