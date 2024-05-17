class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, n - 1):
            return False

            # b=bin(n)
            # if b==b[::-1]:
            #     return True
            # return False
