class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(path):
            if len(path) == n:
                ans.append("".join(path))
                return
            for char in 'abc':
                if not path or path[-1] != char:
                    path.append(char)
                    backtrack(path)
                    path.pop()

        ans = []
        backtrack([])
        
        return ans[k - 1] if k <= len(ans) else ""   