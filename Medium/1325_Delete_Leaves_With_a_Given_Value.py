# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def newNodes(root):
            if not root:
                return None
            root.left = newNodes(root.left)
            root.right = newNodes(root.right)
            if not root.left and not root.right and root.val == target:
                return None
            return root
        root = newNodes(root)
        return root