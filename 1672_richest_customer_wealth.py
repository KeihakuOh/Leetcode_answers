class Solution(object):
    def maximumWealth(self, accounts):
        N = len(accounts)
        max = 0
        for i in range(N):
            if sum(accounts[i]) > max:
                max = sum(accounts[i])
        return max