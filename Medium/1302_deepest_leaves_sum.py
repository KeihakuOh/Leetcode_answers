class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        maxlevel = 0
        tsum = 0

        def dfs(node=root, level=0):
            nonlocal maxlevel, tsum
            if not node:
                return
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
            if maxlevel < level:
                maxlevel = level
                tsum = 0
            if maxlevel == level:
                tsum += node.val

        dfs()
        return tsum
