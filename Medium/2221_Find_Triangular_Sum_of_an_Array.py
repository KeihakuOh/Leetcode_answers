class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        while n != 1:
            new_nums = []
            for j in range(len(nums) - 1):
                new_nums.append((nums[j] + nums[j + 1]) % 10)
            nums = new_nums
            n -= 1
        ans = nums[0]
        return ans
