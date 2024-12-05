class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_num = 0
        for n in nums:
            max_num |= n
        
        def dfs(i, curr):
            if i == len(nums):
                return 1 if curr == max_num else 0 
            count = 0
            count += dfs(i + 1, curr)
            count += dfs(i + 1, nums[i] | curr)
            return count

        return dfs(0, 0)