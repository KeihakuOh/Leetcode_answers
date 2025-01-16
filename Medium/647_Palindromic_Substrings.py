class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            total += self.countPalindromesAroundCenter(i, i, s)
            total += self.countPalindromesAroundCenter(i, i + 1, s)
        return total

    def countPalindromesAroundCenter(self, left, right, s):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count