from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer_dict = defaultdict(list)
        for element in strs:
            s = "".join(sorted(element))
            answer_dict[s].append(element)

        return list(answer_dict.values())
