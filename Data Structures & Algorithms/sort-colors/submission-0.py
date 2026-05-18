class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0] * (max(nums) + 1)
        for n in nums:
            buckets[n] += 1
        idx = 0
        for bucket_number, bucket_count in enumerate(buckets):
            for _ in range(bucket_count):
                nums[idx] = bucket_number
                idx += 1
