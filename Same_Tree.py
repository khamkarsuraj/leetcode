# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Using helper function
    '''
    def helper(self, p, q):
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.helper(p.left, q.left) and self.helper(p.right, q.right)

    def isSameTree(self, p, q) -> bool:
        return self.helper(p, q)
    '''

    # Time Complexity: O(min(p,q)) | Space Complexity: O(log min(p,q))
    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

