from heapq import heapify_max, heappop_max 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify_max(nums)
        i = 0;
        while i<k:
            value = heappop_max(nums)
            i += 1
        return value

        