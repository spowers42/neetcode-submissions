class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        num_rows, num_columns = len(grid), len(grid[0])
        worst_time = 0

        def bfs(row: int, col: int) -> None:
            visited = set()
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            q = deque()
            q.append((row, col))
            visited.add((row, col))
            time = 0

            while len(q) > 0:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 2:
                        return time
                    for dr, dc in directions:
                        r, c = row + dr, col + dc
                        if (
                            r < 0
                            or c < 0
                            or r == num_rows
                            or c == num_columns
                            or (r, c) in visited
                            or grid[r][c] == 0
                        ):
                            continue
                        q.append((r, c))
                        visited.add((r, c))
                time += 1
            return -1

        for row in range(num_rows):
            for col in range(num_columns):
                if grid[row][col] == 1:
                    t = bfs(row, col)
                    if t == -1:
                        return -1
                    worst_time = max(worst_time, t)

        return worst_time
