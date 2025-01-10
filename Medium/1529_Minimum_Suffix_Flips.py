class Solution:
    def minFlips(self, target: str) -> int:
        ans = 0
        current_bit = '0'

        for char in target:
            if char != current_bit:
                ans += 1
                current_bit = char

        return ans
