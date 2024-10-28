# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.val_set = set()
        self.recoverTree(root, 0)

    def recoverTree(self, root: Optional[TreeNode], val: int):
        if root:
            root.val = val
            self.val_set.add(val)
            self.recoverTree(root.left, 2 * val + 1)
            self.recoverTree(root.right, 2 * val + 2)

    def find(self, target: int) -> bool:
        return target in self.val_set


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)