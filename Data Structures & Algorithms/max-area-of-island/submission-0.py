class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows, num_columns = len(grid), len(grid[0])
        visited = set()
        best_size = 0

        def dfs(row: int, column: int) -> int:
            if (
                row < 0
                or column < 0
                or row >= num_rows
                or column >= num_columns
                or (row, column) in visited
                or grid[row][column] == 0
            ):
                return 0
            size = 1
            visited.add((row, column))

            size += dfs(row - 1, column)
            size += dfs(row + 1, column)
            size += dfs(row, column - 1)
            size += dfs(row, column + 1)

            return size

        for row_idx in range(num_rows):
            for col_idx in range(num_columns):
                if (row_idx, col_idx) not in visited and grid[row_idx][col_idx] == 1:
                    size = dfs(row_idx, col_idx)
                    best_size = max(size, best_size)
        return best_size
