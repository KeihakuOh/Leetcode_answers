class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)
        for i in range(len(boxes)):
            sum = 0
            for j in range(len(boxes)):
                if boxes[j] == "1":
                    sum += abs(j - i)
            ans[i] = sum
        return ans