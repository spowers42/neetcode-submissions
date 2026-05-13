from copy import copy


# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return pairs

        result = []
        result.append(copy(pairs))

        for i in range(1, len(pairs)):
            working = copy(result[-1])
            j = i - 1
            while j >= 0 and working[j + 1].key < working[j].key:
                tmp = working[j]
                working[j] = working[j + 1]
                working[j + 1] = tmp
                j -= 1

            result.append(working)
        return result
