class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1 = 0
        idx2 = 0
        end_idx = m  # points to the empty location AFTER numbers in nums1

        while idx1 < end_idx and idx2 < len(nums2):
            if nums1[idx1] <= nums2[idx2]:
                idx1 += 1
            else:
                self.shift(nums1, end_idx, idx1)
                nums1[idx1] = nums2[idx2]
                idx1 += 1
                idx2 += 1
                end_idx += 1

        while idx2 < len(nums2):
            nums1[idx1] = nums2[idx2]
            idx1 += 1
            idx2 += 1

    def shift(self, array: List[int], right_idx: int, left_idx: int):
        # shift everything right up to and including the left index
        while right_idx >= left_idx:
            array[right_idx] = array[right_idx - 1]
            right_idx -= 1
        array[left_idx] = 0  # same as moving the 0 from the right, helpful for debug
