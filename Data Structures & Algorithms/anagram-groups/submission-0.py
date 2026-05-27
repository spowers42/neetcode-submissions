from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        counters = []
        while strs:
            s = strs.pop()
            s_counter = Counter(s)
            appended = False
            for idx in range(len(answer)):
                if s_counter == counters[idx]:
                    answer[idx].append(s)
                    appended = True
                    break
            if not appended:
                counters.append(Counter(s))
                answer.append([s])
        return answer
