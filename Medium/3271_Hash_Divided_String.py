class Solution:
    def stringHash(self, s: str, k: int) -> str:
        n = len(s)
        ans = ''
        for i in range(0, n, k):
            sub = s[i:i+k]
            num = 0
            for char in sub:
                num += (ord(char) - 97)
            new_num = num % 26
            new_char = chr(new_num + 97)
            ans += new_char
        return ans
