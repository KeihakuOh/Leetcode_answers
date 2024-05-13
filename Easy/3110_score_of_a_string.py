class Solution:
    def scoreOfString(self, s: str) -> int:
        sum = 0
        for i in range(len(s)-1):
            ord_1 = ord(s[i])
            ord_2 = ord(s[i + 1])
            sum += abs(ord_1 - ord_2)
        return sum