class Solution:
    def minOperations(self, n: int) -> int:
        mid = n // 2
        if n % 2 == 0:
            return mid ** 2
        else: 
            return mid * (mid + 1)
# Sum = n / 2 * (a1 + an)