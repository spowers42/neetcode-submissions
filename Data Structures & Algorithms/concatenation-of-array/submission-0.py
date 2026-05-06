class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # pythonic answer is nums + nums but lets do it by hand
        new_array = [e for e in nums]  # copy original

        # Add the numbers again
        for element in nums:
            new_array.append(element)
        return new_array
