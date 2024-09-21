class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        num = math.gcd(2, n)
        return int(n * 2 / num)