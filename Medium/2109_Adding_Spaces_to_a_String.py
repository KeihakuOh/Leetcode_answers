class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        m, n = len(spaces), len(s)
        ans = [' '] * (m + n)
        space_index = 0 
        for i, char in enumerate(s):
            if space_index < m and i == spaces[space_index]:
                space_index += 1
            ans[i + space_index] = char
        return "".join(ans)