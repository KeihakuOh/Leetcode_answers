class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        l = []
        for i in nums:
            l.append(int(str(i)[::-1]))
        nums += l
        return len(set(nums))
        