class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        for i in range(1 << n):
            bin_str = format(i, "0" + str(n) + "b")
            if("00" not in bin_str):
                ans.append(bin_str)
        return ans