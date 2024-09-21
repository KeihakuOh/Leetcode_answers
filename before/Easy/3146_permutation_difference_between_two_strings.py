class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        length = len(s)
        sum = 0
        for i in range(length):
            alp = s[i]
            num = t.find(alp)
            sum += abs(i - num)
        return sum