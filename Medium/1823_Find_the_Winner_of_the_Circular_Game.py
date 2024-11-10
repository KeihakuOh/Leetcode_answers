class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        cycle = [i for i in range(1, n + 1)]
        index = 0
        while len(cycle) > 1:
            index = (index + k - 1) % len(cycle)
            cycle.pop(index)
        return cycle[0]