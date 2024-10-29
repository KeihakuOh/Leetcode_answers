class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lis_less = []
        lis_greater = []
        lis_equal = []
        for i in range (len(nums)):
            if nums[i] < pivot:
                lis_less.append(nums[i])
            elif nums[i] > pivot:
                lis_greater.append(nums[i])
            else:
                lis_equal.append(nums[i])
        ans = lis_less + lis_equal + lis_greater
        return ans