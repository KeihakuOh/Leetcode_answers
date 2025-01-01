class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        result = ""
        for i in range(n):
            result += '1' if nums[i][i] == '0' else '0'
        return result