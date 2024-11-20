class Solution:
    def stringSequence(self, target: str) -> List[str]:
        ans = []
        letters="abcdefghijklmnopqrstuvwxyz"
        prev=""
        for char in target:
            i = 0
            while letters[i] != char:
                x = prev + letters[i]
                ans.append(x)
                i += 1
            prev = prev + char
            ans.append(prev)
        return ans