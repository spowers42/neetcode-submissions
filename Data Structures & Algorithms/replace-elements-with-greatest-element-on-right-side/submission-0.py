class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest_right = arr[-1]
        arr[-1] = -1
        for idx in range(len(arr) - 2, -1, -1):
            tmp = arr[idx]
            arr[idx] = largest_right
            largest_right = max(largest_right, tmp)
        return arr
