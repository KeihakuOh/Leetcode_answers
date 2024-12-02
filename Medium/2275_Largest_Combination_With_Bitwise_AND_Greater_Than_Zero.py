class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        mx = 0
        for x in range(24):
            curr = 0
            for num in candidates:
                if (num >> x) & 1:
                    curr += 1
            if curr >=mx:
                mx = curr
        return mx