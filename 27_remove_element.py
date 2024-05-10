class Solution(object):
    def removeElement(self, nums, val):
        length = len(nums)
        count = 0
        for i in range(length):
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return(count)