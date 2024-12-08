class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backstrack(index, path):
            result.append(path)
            for i in range(index, len(nums)):
                backstrack(i + 1, path + [nums[i]])

        result = []
        backstrack (0, [])
        return result