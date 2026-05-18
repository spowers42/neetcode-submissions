from math import sqrt


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self._quicksort(points, 0, len(points) - 1, k)
        return points[:k]

    def _quicksort(self, points: List[List[int]], start_idx: int, end_idx: int, k: int) -> None:
        if end_idx <= start_idx:
            return

        pivot_val = points[end_idx]
        pivot_dist = self._distance(pivot_val)

        write_idx = start_idx
        for read_idx in range(start_idx, end_idx):
            if self._distance(points[read_idx]) < pivot_dist:
                points[write_idx], points[read_idx] = points[read_idx], points[write_idx]
                write_idx += 1
        points[write_idx], points[end_idx] = points[end_idx], points[write_idx]
        self._quicksort(points, start_idx, write_idx - 1, k)
        if write_idx < k:
            self._quicksort(points, write_idx + 1, end_idx, k)

    def _distance(self, point: List[int]) -> float:
        return point[0] ** 2 + point[1] ** 2
