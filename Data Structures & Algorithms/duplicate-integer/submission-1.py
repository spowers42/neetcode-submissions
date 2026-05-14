class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        value_dict = {}
        for index, value in enumerate(nums):
            if value in value_dict:
                return True
            value_dict[value] = index

        return False
