class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = k
        for num in nums:
            count ^= num
        ans = 0
        while   count:
            ans +=  count & 1
            count >>= 1
        return ans