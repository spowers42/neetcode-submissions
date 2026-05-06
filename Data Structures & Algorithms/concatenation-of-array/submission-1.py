class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # pythonic answer is nums + nums but lets do it by hand
        size = len(nums)
        new_array = [0] * (2*size)
        for i, element in enumerate(nums):
            new_array[i] = element
            new_array[i+size] = element
        return new_array
