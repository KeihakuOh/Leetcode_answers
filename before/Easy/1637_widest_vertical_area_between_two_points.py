class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        l = []
        for i in range(len(points)):
            l.append(points[i][0])
        l.sort()
        if(len(l) == 0 or len(l) == 1):
            return 0
        max = 0
        for i in range(len(l) - 1):
            num = l[i + 1] - l[i]
            if num > max:
                max = num
        return max      