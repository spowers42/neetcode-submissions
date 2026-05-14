# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs or len(pairs) == 1:
            return pairs

        middle = len(pairs) // 2
        a = self.mergeSort(pairs[:middle])
        b = self.mergeSort(pairs[middle:])
        return self.merge(a, b)

    def merge(self, a: List[Pair], b: list[Pair]) -> list[Pair]:
        results = []
        a_idx, b_idx = 0, 0
        a_end, b_end = len(a), len(b)
        while a_idx < a_end and b_idx < b_end:
            if a[a_idx].key <= b[b_idx].key:
                results.append(a[a_idx])
                a_idx += 1
            else:
                results.append(b[b_idx])
                b_idx += 1

        if a_idx < a_end:
            results.extend(a[a_idx:])
        elif b_idx < b_end:
            results.extend(b[b_idx:])
        return results
