class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [0] * length
        for i in range(length):
            num = nums[nums[i]]
            ans[i] = num
        return ans