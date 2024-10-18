class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev = 0
        for i in bank:
            c = i.count('1')
            if c:
                ans += c * prev
                prev = c
        return ans