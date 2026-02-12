# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        cnt = 0

        # post order traversal
        def dfs(node):
            nonlocal cnt
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            total_sum = left_sum + right_sum
            if total_sum == node.val:
                cnt += 1
            return total_sum
        dfs(root)
        return cnt