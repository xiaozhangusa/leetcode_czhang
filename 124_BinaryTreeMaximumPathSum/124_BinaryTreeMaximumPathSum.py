# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

# The path sum of a path is the sum of the node's values in the path.

# Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

# Example 1:


# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
# Example 2:


# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 3 * 104].
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 
        self.max_gain = float('-inf')
        self.gain_from_subtree(root)
        return self.max_gain
        
    def gain_from_subtree(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left_gain = max(0, self.gain_from_subtree(node.left))
        right_gain= max(0, self.gain_from_subtree(node.right))
        # case 1: the max path sum includes the current node and its left child
        # case 2: the max path sum includes the current node and its right child
        # case 3: the max path sum includes the current node that both left and right children dont' add positive gain to the path
        # case 4: the max path sum includes the current node and path from both left and right and stop at the current node
        self.max_gain = max(self.max_gain, left_gain + node.val, right_gain + node.val, left_gain + right_gain + node.val, node.val)
        return max(left_gain + node.val, right_gain + node.val, node.val)