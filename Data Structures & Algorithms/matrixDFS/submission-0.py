class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        num_rows, num_columns = len(grid), len(grid[0])
        visited = set()

        def dfs(row: int, column: int) -> int:
            loc = (row, column)
            if (
                row < 0
                or column < 0
                or row == num_rows
                or column == num_columns
                or loc in visited
                or grid[row][column] == 1
            ):
                return 0
            if row == num_rows - 1 and column == num_columns - 1:
                return 1

            paths = 0
            visited.add(loc)

            paths += dfs(row + 1, column)
            paths += dfs(row - 1, column)
            paths += dfs(row, column + 1)
            paths += dfs(row, column - 1)
            visited.remove(loc)
            return paths

        return dfs(0, 0)
