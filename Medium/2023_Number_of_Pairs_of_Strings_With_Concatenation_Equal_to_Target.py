class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num in nums:
            if target.startswith(num):
                suffix = target[len(num):]
                if suffix in freq:
                    count += freq[suffix]
                    if num == suffix:
                        count -= 1

        return count