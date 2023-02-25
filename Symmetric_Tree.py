# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Approch 1: Recursive solution
    # Time complexity: O(n) | Space Complexity: O(logn) OR O(h) where h is height of tree
    def helper(self, l, r):
        if l is None and r is None:
            return True
        
        if l and r and l.val == r.val:
            return self.helper(l.left, r.right) and self.helper(l.right, r.left)
        
        return False

    def isSymmetric(self, root) -> bool:
        return self.helper(root, root)
