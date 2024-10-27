# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        level = 0
        val = []
        while q:
            num = len(q)
            for _ in range(num):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                    q.append(curr.right)
                    if level % 2 == 0:
                        val.append(curr.left.val)
                        val.append(curr.right.val)
                if level % 2 == 1:
                    curr.val = val.pop()
            level += 1
        return root