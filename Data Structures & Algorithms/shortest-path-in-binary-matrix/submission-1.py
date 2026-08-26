class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        num_rows, num_columns = len(grid), len(grid[0])
        visited = set()
        q = deque()
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        if grid[0][0] == 1 or grid[num_rows - 1][num_columns - 1] == 1:
            return -1

        path_length = 1
        q.append((0, 0))
        visited.add((0, 0))

        while len(q) > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                if row == num_rows - 1 and col == num_columns - 1:
                    return path_length

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        r < 0
                        or c < 0
                        or r == num_rows
                        or c == num_columns
                        or (r, c) in visited
                        or grid[r][c] == 1
                    ):
                        continue
                    q.append((r, c))
                    visited.add((r, c))
            path_length += 1

        return -1
