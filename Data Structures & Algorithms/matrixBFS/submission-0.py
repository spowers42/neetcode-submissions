class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        num_rows, num_columns = len(grid), len(grid[0])
        q = deque()
        visited = set()
        length = 0

        if grid[0][0] == 0:
            q.append((0, 0))
            visited.add((0, 0))

        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                if row == num_rows - 1 and col == num_columns - 1:
                    return length
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (
                        r < 0
                        or col < 0
                        or r == num_rows
                        or c == num_columns
                        or (r, c) in visited
                        or grid[r][c] == 1
                    ):
                        continue
                    q.append((r, c))
                    visited.add((r, c))
            length += 1

        return -1
