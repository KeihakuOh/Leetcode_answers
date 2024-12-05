class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        isAns = [True] * n
        ans = []
        for (srcNode, dstNode) in edges:
            isAns[dstNode] = False
        for i, node in enumerate(isAns):
            if node == True:
                ans.append(i)
        return ans