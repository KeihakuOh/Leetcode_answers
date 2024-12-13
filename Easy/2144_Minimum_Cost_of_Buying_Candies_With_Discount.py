class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        total_cost = 0
        for i in range(len(cost)):
            if self.should_add_to_total(i):
                total_cost += cost[i]
        return total_cost
    
    def should_add_to_total(self, index):
        return index % 3 != 2