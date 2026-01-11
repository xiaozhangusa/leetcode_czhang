# If the depth of a tree is smaller than 5, then this tree can be represented by an array of three-digit integers. You are given an ascending array nums consisting of three-digit integers representing a binary tree with a depth smaller than 5, where for each integer:

# The hundreds digit represents the depth d of this node, where 1 <= d <= 4.
# The tens digit represents the position p of this node within its level, where 1 <= p <= 8, corresponding to its position in a full binary tree.
# The units digit represents the value v of this node, where 0 <= v <= 9.
# Return the sum of all paths from the root towards the leaves.

# It is guaranteed that the given array represents a valid connected binary tree.

 

# Example 1:



# Input: nums = [113,215,221]

# Output: 12

# Explanation:

# The tree that the list represents is shown.
# The path sum is (3 + 5) + (3 + 1) = 12.

# Example 2:



# Input: nums = [113,221]

# Output: 4

# Explanation:

# The tree that the list represents is shown. 
# The path sum is (3 + 1) = 4.
# from collections import defaultdict
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        # build tree
        tree = defaultdict(dict)
        for num in nums:
            depth = num // 100
            pos = (num // 10) % 10
            val = num % 10
            if depth not in tree:
                tree[depth] = {}
            # pos // 2 is the parent of pos.
            parent = math.ceil(pos / 2)
            if parent in tree[depth-1]:
                tree[depth][pos] = val + tree[depth-1][parent]
        print(tree)
        pathSum = 0
        for depth in tree:
            for pos in tree[depth]:
                if depth+1 not in tree or (tree[depth+1].get(pos*2) is None and tree[depth+1].get(pos*2+1) is None):
                    pathSum += tree[depth][pos]
        return pathSum