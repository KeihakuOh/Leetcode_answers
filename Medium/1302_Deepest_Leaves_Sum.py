# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self, sum=0, max_level=0):
        self.sum = 0
        self.max_level = 0

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.calSum(0, root)
        return self.sum

    def calSum(self, level, node: Optional[TreeNode]):
        level += 1
        if not node:
            return
        else:
            self.calSum(level, node.left)
            self.calSum(level, node.right)
        if level > self.max_level:
            self.max_level = level
            self.sum = 0
        if self.max_level == level:
            self.sum += node.val


