class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum([1 for h in hours if h>=target])
        # ans = 0
        # for i in range(len(hours)):
        #     if hours[i] >= target:
        #         ans += 1
        # return ans