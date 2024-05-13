class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        nums_ans = [[0] for _  in range(2 * length)]
        for i in range(length):
            nums_ans[i] = nums[i]
            nums_ans[i + length] = nums[i]
        return nums_ans

    # def getConcatenation(self, nums: List[int]) -> List[int]:
    #     return nums + nums 