
# Implementation using a Hash Set (The "Memory Wall" approach)
# Time Complexity: O(N) where N is the number of nodes.
# Space Complexity: O(N) to store the visited values.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        """
        Think of this as walking through a village and checking your notebook (seen set)
        to see if any previously met villager matches the current one to reach the sum k.
        """
        seen = set()
        
        def dfs(node):
            if not node:
                return False
            
            # The "Complement Check": Do we have the match in our notebook?
            complement = k - node.val
            if complement in seen:
                return True
            
            # Record this villager and keep searching
            seen.add(node.val)
            
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)

# Alternative: In-order + Two Pointers (The "Sorting the Queue" approach)
# 1. Flatten the BST into a sorted list using in-order traversal.
# 2. Use two pointers (left and right) to find the target sum.
# Time: O(N), Space: O(N)

class Solution2:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        """
        Think of this as lining up all villagers by age in a straight line (Sorted Array).
        Then, we use two scouts (Pointers) at both ends to find the match.
        """
        nums = []
        
        # In-order traversal of BST gives us elements in ascending order
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
            
        inorder(root)
        
        # Two-pointer movement
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == k:
                return True
            elif current_sum < k:
                left += 1  # Need a bigger sum, move left pointer forward
            else:
                right -= 1 # Need a smaller sum, move right pointer backward
                
        return False
