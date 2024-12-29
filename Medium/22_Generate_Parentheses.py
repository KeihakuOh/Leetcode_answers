class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(cur, open_count, close_count):
            if open_count == n and close_count == n:
                ans.append(cur)
            if open_count < n:
                backtrack(cur + '(', open_count + 1, close_count)
            if close_count < open_count:
                backtrack(cur + ')', open_count, close_count + 1)

        backtrack("", 0, 0)
        return ans