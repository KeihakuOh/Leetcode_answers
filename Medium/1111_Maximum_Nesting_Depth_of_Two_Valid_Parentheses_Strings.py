class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ans = []
        depth = 0
        for char in seq:
            if char == '(':
                ans.append(depth % 2)
                depth += 1
            else:
                depth -= 1
                ans.append(depth % 2)
        return ans