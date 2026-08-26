class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_rows, num_columns = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        fresh = 0
        time = 0

        for r in range(num_rows):
            for c in range(num_columns):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        while q and fresh:
            for _ in range(len(q)):
                row, col = q.popleft()

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r < 0 or c < 0 or r == num_rows or c == num_columns or grid[r][c] != 1:
                        continue
                    grid[r][c] = 2
                    q.append((r, c))
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1
