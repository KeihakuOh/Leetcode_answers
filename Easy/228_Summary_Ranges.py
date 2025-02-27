class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ranges = []
        start = nums[0]
        for i in range(1, len(nums)):
            # Check if the current number is not consecutive to the previous number.
            if nums[i] != nums[i - 1] + 1:
                ranges.append(self.formatRange(start, nums[i - 1]))
                start = nums[i]

        # After the loop, add the last range to the list.
        ranges.append(self.format_range(start, nums[-1]))
        return ranges

    def formatRange(self, start, end):
        return str(start) if start == end else f"{start}->{end}"