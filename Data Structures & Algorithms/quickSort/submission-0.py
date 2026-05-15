# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs or len(pairs) == 1:
            return pairs

        self._quicksort(pairs, 0, len(pairs) - 1)
        return pairs

    def _quicksort(self, array: List[Pair], start_idx: int, end_idx: int) -> None:
        if start_idx >= end_idx:
            return

        pivot = array[end_idx]
        read_idx = start_idx
        write_idx = start_idx

        while read_idx < end_idx:
            if array[read_idx].key < pivot.key:
                array[read_idx], array[write_idx] = array[write_idx], array[read_idx]
                write_idx += 1
            read_idx += 1

        array[write_idx], array[end_idx] = array[end_idx], array[write_idx]

        # sort the two sides
        self._quicksort(array, start_idx, write_idx - 1)
        self._quicksort(array, write_idx + 1, end_idx)
