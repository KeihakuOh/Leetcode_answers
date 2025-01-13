class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)    
        diff_s_to_t = count_s - count_t
        diff_t_to_s = count_t - count_s
        ans = sum(diff_s_to_t.values()) + sum(diff_t_to_s.values())
        return ans