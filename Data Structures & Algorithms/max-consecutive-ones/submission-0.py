class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        current_consecutive = 0
        for element in nums:
            if element == 1:
                current_consecutive += 1
            else:
                if current_consecutive > max_consecutive:
                    max_consecutive = current_consecutive
                current_consecutive = 0
        if current_consecutive > max_consecutive:
            return current_consecutive
        return max_consecutive