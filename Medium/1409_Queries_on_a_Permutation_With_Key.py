class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        ans = []
        lis = []
        for i in range(1, m + 1):
            lis.append(i)
        for i in queries:
            ans.append(lis.index(i))
            lis.remove(i)
            lis.insert(0,i)
        return ans
