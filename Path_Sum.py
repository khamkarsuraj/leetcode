# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], TargetSum: int) -> bool:
        # return False if tree is empty
        # also, if current node has no left or right node
        if root is None:
            return False
        
        # once reached leaf node, check if we got TargetSum else return False
        if root.left is None and root.right is None:
            return TargetSum == root.val

        # first check for left side node and then right, substracting current node val
        return self.hasPathSum(root.left, TargetSum - root.val) or self.hasPathSum(root.right, TargetSum - root.val)
