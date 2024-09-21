class Solution:
    def defangIPaddr(self, address: str) -> str:
        length = len(address)
        ans = ""
        for i in range(length):
            if address[i] == ".":
                ans += "[.]"
            else:
                ans += address[i]
        return ans