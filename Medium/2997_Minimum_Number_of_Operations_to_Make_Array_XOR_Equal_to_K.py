class Solution:   
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in nums:
            ans ^= i
        ans = ans ^ k
        return bin(ans).count('1')