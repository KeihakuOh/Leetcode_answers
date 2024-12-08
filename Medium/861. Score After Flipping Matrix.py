class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for row in grid:
            if row[0] == 0:
                for j in range(len(row)):
                    row[j] = 1 - row[j]
        num_rows = len(grid)
        num_cols = len(grid[0])
        ans = 0
        for j in range(num_cols):
            ones_count = sum(row[j] for row in grid)
            max_count = max(ones_count, num_rows - ones_count)
            ans += max_count * (2 ** (num_cols - 1 - j))
        return ans
