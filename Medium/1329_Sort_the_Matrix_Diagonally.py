class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])  
        diagonals = {}  
    
        for i in range(n):
            for j in range(m):
                key = i - j
                if key not in diagonals:
                    diagonals[key] = []
                diagonals[key].append(mat[i][j])
        
        for key in diagonals:
            diagonals[key].sort()

        for i in range(n):
            for j in range(m):
                key = i - j
                mat[i][j] = diagonals[key].pop(0)
        
        return mat
