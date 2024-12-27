class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_ans = 0
        for row in grid:
            for i in range(n // 2):
                row_ans += row[i] ^ row[n - 1 - i]
        col_ans = 0
        for j in range(n):
            for i in range(m // 2):
                col_ans += grid[i][j] ^ grid[m - 1 - i][j]
        return min(row_ans, col_ans)
