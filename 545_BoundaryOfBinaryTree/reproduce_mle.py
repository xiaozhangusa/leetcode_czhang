import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(vals):
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = collections.deque([root])
    i = 1
    while queue and i < len(vals):
        node = queue.popleft()
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root

from typing import List, Optional
from collections import deque

class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        # The current implementation has infinite loops in leftBoundary and rightBoundary
        # and incorrect leaf ordering and duplicates.
        try:
            return self.leftBoundary(root) + self.leaves(root) + self.rightBoundary(root)
        except Exception as e:
            return str(e)
    
    def leftBoundary(self, root: Optional[TreeNode]) -> List[int]:
        if not root.left and not root.right:
            return []
        res = []
        count = 0
        while root:
            res.append(root.val)
            # pursue left child if possible, otherwise pursue right child
            if root.left:
                root = root.left
            # if left child is not possible, pursue right child
            elif root.right:
                root = root.right
            
            count += 1
            if count > 100:
                print("Infinite loop detected in leftBoundary")
                break
        return res
    
    def rightBoundary(self, root: Optional[TreeNode]) -> List[int]:
        if not root.left and not root.right:
            return []
        res = []
        count = 0
        while root:
            res.append(root.val)
            if root.right:
                root = root.right
            elif root.left:
                root = root.left
            
            count += 1
            if count > 100:
                print("Infinite loop detected in rightBoundary")
                break
        return res
    
    def leaves(self, root: Optional[TreeNode]) -> List[int]:
        # if root is a leaf, return [root.val]
        if not root.left and not root.right:
            return [root.val]
        q = deque()
        q.append(root)
        res = []
        while q:
            node = q.popleft()
            if not node.left and not node.right:
                res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res

if __name__ == "__main__":
    sol = Solution()
    root = build_tree([1, None, 2, 3, 4])
    print("Testing root = [1, null, 2, 3, 4]")
    result = sol.boundaryOfBinaryTree(root)
    print("Result:", result)
