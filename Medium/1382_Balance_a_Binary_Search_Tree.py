# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        def dfs(node):
            nonlocal nodes
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            nodes.append(node.val)

        def add(nodes, start, end):
            if start > end:
                return
            middle = (start + end)
            node = TreeNode(nodes[middle])
            node.left = add(nodes, start, middle - 1)
            node.right = add(nodes, middle + 1, end)
            return node
        
        dfs(root)

        result = add(nodes, 0, len(nodes) - 1)

        return result   