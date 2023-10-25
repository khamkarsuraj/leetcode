# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Recursion
    #Time: O(n)
    #Space: O(1)
    def depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return max(self.depth(root.left), self.depth(root.right))+1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth(root)
