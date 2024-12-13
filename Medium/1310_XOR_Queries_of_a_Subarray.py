class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        pref = [0] * (n + 1)
        ans = []
        for i in range(1, n + 1):
            pref[i] = arr[i - 1] ^ pref[i - 1]
        for l, r in queries:
            ans.append(pref[l] ^ pref[r + 1])
        return ans