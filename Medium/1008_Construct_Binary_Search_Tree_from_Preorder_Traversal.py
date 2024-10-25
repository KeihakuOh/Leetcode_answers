# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None 

        root = TreeNode(preorder[0])

        ind = 1
        for i in range(1, len(preorder)):
            if preorder[i] > preorder[0]:
                break
            else:
                ind += 1
        root.left = self.bstFromPreorder(preorder[1:ind])
        root.right = self.bstFromPreorder(preorder[ind:])

        return root
        