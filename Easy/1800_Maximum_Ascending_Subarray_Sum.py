class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            if self.is_ascending(nums[i], nums[i - 1]):
                current_sum += nums[i]
            else:
                current_sum = nums[i]
            max_sum = max(max_sum, current_sum)
        
        return max_sum

    def is_ascending(self, curr: int, prev: int) -> bool:
        return curr > prev