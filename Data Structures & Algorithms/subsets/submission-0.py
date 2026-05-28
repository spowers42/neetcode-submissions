from copy import copy


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            for idx in range(len(result)):
                a = copy(result[idx])
                a.append(num)
                result.append(a)
        return result
