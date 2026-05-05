class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        tail_idx = len(nums)-1
        while idx<=tail_idx:
            if nums[idx] == val:
                nums[idx] = nums[tail_idx]
                tail_idx -= 1
            else:
                idx += 1

        return idx
