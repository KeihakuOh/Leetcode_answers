class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        for i in range (len(arr)):
            xor = arr[i]
            for j in range(i + 1, len(arr)):
                xor ^= arr[j]
                if xor == 0:
                    ans += j - i
        return ans