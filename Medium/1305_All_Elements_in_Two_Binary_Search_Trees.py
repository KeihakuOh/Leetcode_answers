# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if node:
                ans.append(node.val)
                dfs(node.left)
                dfs(node.right)
        
        ans = []

        dfs(root1)
        dfs(root2)

        return sorted(ans)