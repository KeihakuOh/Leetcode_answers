class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans = []
        mask = (1 << maximumBit) - 1
        for x in nums:
            ans.append(x ^ mask)
            mask = mask ^ x
        ans.reverse()
        return ans