class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = []
        for i in range(len(queries)):
            x, y, r = queries[i]
            count = 0
            for X, Y in points:
                if ((X - x)**2 + (Y - y)**2)**0.5 <= r:
                    count += 1
            ans.append(count)
        return ans