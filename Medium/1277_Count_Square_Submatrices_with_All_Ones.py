class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        ans = 0
        for i in range(n):
            for j in range(m):
                if i != 0 and j != 0 and matrix[i][j] == 1:
                    matrix[i][j] += min(matrix[i - 1][ j - 1], matrix[i - 1][j], matrix[i][j - 1]) 
                ans += matrix[i][j]
        return ans