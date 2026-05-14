# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs or len(pairs) == 1:
            return pairs
        return self._mergesort(pairs, 0, len(pairs) - 1)

    def _mergesort(self, pairs: List[Pair], start: int, end: int) -> list[Pair]:
        if end - start <= 0:
            return pairs

        middle = (start + end) // 2
        self._mergesort(pairs, start, middle)
        self._mergesort(pairs, middle + 1, end)
        self._merge(pairs, start, middle, end)
        return pairs

    def _merge(self, pairs: List[Pair], start_idx: int, middle_idx: int, end_idx: int) -> None:
        left_idx, right_idx = 0, 0
        pairs_ptr = start_idx
        left = pairs[start_idx : middle_idx + 1]
        right = pairs[middle_idx + 1 : end_idx + 1]

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx].key <= right[right_idx].key:
                pairs[pairs_ptr] = left[left_idx]
                left_idx += 1
            else:
                pairs[pairs_ptr] = right[right_idx]
                right_idx += 1
            pairs_ptr += 1
        while left_idx < len(left):
            pairs[pairs_ptr] = left[left_idx]
            left_idx += 1
            pairs_ptr += 1
        while right_idx < len(right):
            pairs[pairs_ptr] = right[right_idx]
            right_idx += 1
            pairs_ptr += 1
