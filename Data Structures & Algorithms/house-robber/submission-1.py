class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def dfs(idx: int):
            if idx >= len(nums):
                return 0
            if idx in cache:
                return cache[idx]

            # skip the current and go to the next
            a = dfs(idx + 1)
            # this one and then skip next
            b = nums[idx] + dfs(idx + 2)
            cache[idx] = max(a, b)
            return cache[idx]

        return dfs(0)
