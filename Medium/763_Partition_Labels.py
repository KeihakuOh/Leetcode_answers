class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_position = {char: i for i, char in enumerate(s)}
        ans = []
        start, end = 0, 0
        for i, char in enumerate(s):
            end = max(end, last_position[char])
            if i == end:
                ans.append(end - start + 1)
                start = end + 1
        return ans
            
            