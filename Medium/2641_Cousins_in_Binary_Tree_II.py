# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([(root, None)]) 

        while queue:
            level_nodes = [] 
            level_sum = 0
            parent_to_sum = defaultdict(int)
            for _ in range(len(queue)):
                node, parent = queue.popleft()
                level_nodes.append((node, parent))
                level_sum += node.val

                if parent:
                    parent_to_sum[parent] += node.val 

                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))

            for node, parent in level_nodes:
                if parent:
                    node.val = level_sum - parent_to_sum[parent]
                else:
                    node.val = 0
        return root