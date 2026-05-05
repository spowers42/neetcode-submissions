class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences: dict[int, int] = {}
        for index in range(0, len(nums)):
            d = target-nums[index]
            index2 = differences.get(d)
            if index2 is not None:
                result = [index, index2]
                return sorted(result)
            differences[nums[index]] = index
