from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def to_key(s: str) -> tuple[int]:
            counts = [0] * 26
            for char in s:
                idx = ord(char) - ord("a")
                counts[idx] += 1
            return tuple(counts)

        answer_dict = defaultdict(list)
        for s in strs:
            key = to_key(s)
            answer_dict[key].append(s)

        return list(answer_dict.values())
