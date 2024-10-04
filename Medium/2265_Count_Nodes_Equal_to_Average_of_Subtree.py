# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.result = 0
        self.helper(root)
        return self.result

    def helper(self, root: TreeNode):
        if not root:
            return (0, 0)
        
        left_sum, left_count = self.helper(root.left)
        right_sum, right_count = self.helper(root.right)

        total_sum = left_sum + right_sum + root.val
        total_count = left_count + right_count + 1

        if root.val == total_sum // total_count:
            self.result += 1

        return (total_sum, total_count)