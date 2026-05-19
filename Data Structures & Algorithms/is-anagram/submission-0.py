class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # the simple python solution is to use Counter but instead lets write it by hand
        s_counts = self._get_counts(s)
        t_counts = self._get_counts(t)

        for char, count in s_counts.items():
            if char in t_counts and t_counts[char] == count:
                del t_counts[char]
            else:
                return False
        if t_counts:
            return False
        return True

    def _get_counts(self, string: str) -> dict:
        d = dict()
        for char in string:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        return d
