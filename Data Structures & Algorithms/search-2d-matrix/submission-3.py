class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top_row = 0
        bottom_row = len(matrix) - 1

        while top_row <= bottom_row:
            middle_row = (top_row + bottom_row) // 2
            if matrix[middle_row][0] > target:
                bottom_row = middle_row - 1
            elif matrix[middle_row][-1] < target:
                top_row = middle_row + 1
            else:
                return self.quicksort(matrix[middle_row], target)
        return False

    def quicksort(self, row: List[int], target: int) -> bool:
        left, right = 0, len(row) - 1

        while left <= right:
            middle = (left + right) // 2

            if row[middle] < target:
                left = middle + 1
            elif row[middle] > target:
                right = middle - 1
            else:
                return True
        return False
