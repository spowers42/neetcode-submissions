from copy import copy


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        working = []

        def dfs(i: int) -> None:
            if i >= len(nums):
                result.append(working.copy())
                return
            working.append(nums[i])
            dfs(i + 1)
            working.pop()
            dfs(i + 1)

        dfs(0)
        return result
