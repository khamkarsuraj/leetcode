# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursion
    # Time: O(n) n is no of nodes
    # Space: O(h) h is height of tree
    def validate(self, node, lower, upper):
        if not node:
            return True

        if node.val > lower and node.val < upper:
            return self.validate(node.left, lower, node.val) and self.validate(node.right, node.val, upper)

        return False

    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root, float("-inf"), float("+inf"))
