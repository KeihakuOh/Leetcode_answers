class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        def isArithmetic(lis):
            lis.sort()
            diff = lis[1] - lis[0]
            for i in range(2, len(lis)):
                if lis[i] - lis[i - 1] != diff:
                    return False
            return True

        for i in range(len(l)):
            ans.append(isArithmetic(nums[l[i]:r[i]+1]))

        return ans