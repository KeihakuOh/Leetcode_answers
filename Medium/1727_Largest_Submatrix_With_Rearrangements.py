class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        self.compute_height_matrix(matrix, rows, cols)
        max_area = 0

        for row in matrix:
            row.sort(reverse=True)  
            for width in range(cols):
                height = row[width]
                max_area = max(max_area, height * (width + 1))

        return max_area

    def compute_height_matrix(self, matrix: List[List[int]], rows: int, cols: int) -> None:
        for r in range(1, rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    matrix[r][c] += matrix[r - 1][c]