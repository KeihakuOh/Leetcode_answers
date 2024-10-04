class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = []
        while nums:
            checked_num = set()
            lis = []
            remaining = []
            for num in nums:
                if num not in checked_num:
                    lis.append(num)
                    checked_num.add(num)
                else:
                    remaining.append(num)
            nums = remaining
            ans.append(lis)
        return ans
