# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        pre_val = 0  
        def calSub(root: TreeNode):
            nonlocal pre_val  
            if root:
                calSub(root.left)  
                root.val, pre_val = -pre_val, pre_val + root.val
                calSub(root.right)  
        def calAns(root: TreeNode):
            nonlocal pre_val  
            if root:
                root.val += pre_val
                calAns(root.left)
                calAns(root.right)
        calSub(root)
        calAns(root)
        return root
