class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = [[0] * n for _ in range(m)]
        sum_m = [sum(i) for i in grid]
        sum_n = [sum(k[i] for k in grid) for i in range(n)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = sum_m[i] + sum_n[j] - (n - sum_m[i]) - (m - sum_n[j])
        return ans