class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        pointer = 1
        ans = []
        for num in target:
            ans.extend(["Push", "Pop"] * (num-pointer))
            ans.append("Push")
            pointer = num + 1
        return ans