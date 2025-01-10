class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_index = 0
        s_index = 0
        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]: 
                t_index += 1
            s_index += 1
        return len(t) - t_index