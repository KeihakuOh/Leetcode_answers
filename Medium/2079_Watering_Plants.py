class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        rest = capacity
        for i, x in enumerate(plants): 
            if x > rest:
                rest = capacity - x
                ans += 2 * i + 1
            else:
                rest -= x
                ans += 1 
        return ans
            