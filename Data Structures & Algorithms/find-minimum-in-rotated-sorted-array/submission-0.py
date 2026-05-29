class Solution:
    def findMin(self, nums: List[int]) -> int:
        best = nums[0]

        def search(l, r):
            nonlocal best
            if l < r:
                mid = (l + r) // 2
                if nums[r] < nums[mid]:
                    best = nums[r]
                    return search(mid + 1, r)
                else:
                    best = nums[mid]
                    return search(l, r - 1)

        search(0, len(nums) - 1)
        return best
