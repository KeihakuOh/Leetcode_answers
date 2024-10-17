# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, grand: int, parent: int):
            if not root:
                return 0
            sum = 0
            if (grand % 2 == 0):
                sum = root.val
            sum += dfs(root.left, parent, root.val)
            sum += dfs(root.right, parent, root.val)

            return sum

        return dfs(root, 1, 1)