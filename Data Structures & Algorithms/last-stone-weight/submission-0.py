from heapq import heapify_max, heappush_max, heappop_max


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapify_max(stones)
        while len(stones) > 1:
            x = heappop_max(stones)
            y = heappop_max(stones)
            z = x - y
            if z == 0:
                continue
            heappush_max(stones, z)
        if len(stones) == 1:
            return stones[0]
        return 0
