# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # dfs using recursion
        # time n
        # space h
        max_dia = 0

        def dfs(root):
            if not root:
                return 0
    
            left_height = dfs(root.left)
            right_height = dfs(root.right)

            curr_dia = left_height + right_height

            nonlocal max_dia
            max_dia = max(max_dia, curr_dia)
            return 1 + max(left_height, right_height)
        
        dfs(root)
        return max_dia
543. Diameter of Binary Tree
