class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s)).lower()

        left_idx, right_idx = 0, len(s) - 1
        while left_idx < right_idx:
            if s[left_idx] != s[right_idx]:
                return False
            left_idx += 1
            right_idx -= 1
        return True
