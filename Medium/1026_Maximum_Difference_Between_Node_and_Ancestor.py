# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        global ans
        ans = 0

        def caul(node, mx, mn):
            global ans
            if not node:
                ans = max(ans, abs(mx - mn))
                return
            if node.val < mn:
                mn = node.val
            elif node.val > mx:
                mx = node.val
            val = abs(mx - mn)
            if val > ans:
                ans = val
            caul(node.left, mx, mn)
            caul(node.right, mx, mn)

        caul(root, root.val, root.val)
        return ans