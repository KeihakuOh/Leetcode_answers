class Solution:
    def minSteps(self, s: str, t: str) -> int:
        num = (Counter(s) & Counter(t)).total()
        sub = len(s) - num
        return sub