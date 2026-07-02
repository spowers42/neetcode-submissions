from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        sorted_counts = sorted(counter.items(),  key=lambda t: -t[1])
        return [k for k, _ in sorted_counts[:k]]