class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                min_num = min(rowSum[i], colSum[j])
                ans[i][j] = min_num
                rowSum[i] -= min_num
                colSum[j] -= min_num
        return ans