class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        def calculate_sum(i, k, n, code):
            total = 0
            if k > 0:
                for j in range(1, k + 1):
                    total += code[(i + j) % n]
            else:
                for j in range(1, 1 - k):
                    total += code[(i - j) % n]
            return total
        n = len(code)
        if k == 0:
            return [0] * n
        else:
            return [calculate_sum(i, k, n, code) for i in range(n)] 

