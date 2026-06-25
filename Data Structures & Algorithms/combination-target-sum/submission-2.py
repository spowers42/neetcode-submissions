class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        working = []
        s = 0
        l = len(nums)
        nums.sort()

        def dfs(idx: int):
            nonlocal s
            if s == target:
                results.append(working.copy())
                return

            for n in range(idx, l):
                if s+nums[n] > target:
                    return
                working.append(nums[n])
                s += nums[n]
                dfs(n)
                # undo this branches work
                v = working.pop()
                s -= v

        dfs(0)
        return results
