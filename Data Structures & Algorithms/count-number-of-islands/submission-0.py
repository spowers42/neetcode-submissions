class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_rows = len(grid)
        n_columns = len(grid[0])
        island_count = 0

        def dfs(y: int, x: int):
            if x < 0 or x >= n_columns or y < 0 or y >= n_rows:
                return 0
            elif grid[y][x] == "0":
                return 0

            grid[y][x] = "0"

            dfs(y + 1, x)
            dfs(y - 1, x)
            dfs(y, x + 1)
            dfs(y, x - 1)

            return 1

        for row in range(n_rows):
            for column in range(n_columns):
                island_count += dfs(row, column)

        return island_count
