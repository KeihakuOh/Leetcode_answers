class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def dfs(index, path):
            if index == len(graph) - 1:
                ans.append(path)
            else:
                for i in graph[index]:
                    dfs(i, path + [i])
        dfs(0, [0])
        return ans
