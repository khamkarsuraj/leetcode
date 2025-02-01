# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # understand why we pass min_val and max_val on line 23 (imp line)
        # dfs
        # time n
        # space h
        def dfs(min_val, root, max_val):
            if not root:
                return True
        
            if not root.val > min_val:
                return False
            
            if not root.val < max_val:
                return False

            return dfs(min_val, root.left, root.val) and dfs(root.val, root.right, max_val) #imp line
        
        return dfs(float('-inf'), root, float('inf'))
    
    # # Recursion
    # # Time: O(n) n is no of nodes
    # # Space: O(h) h is height of tree
    # def validate(self, node, lower, upper):
    #     if not node:
    #         return True

    #     if node.val > lower and node.val < upper:
    #         return self.validate(node.left, lower, node.val) and self.validate(node.right, node.val, upper)

    #     return False

    # def isValidBST(self, root: TreeNode) -> bool:
    #     return self.validate(root, float("-inf"), float("+inf"))
    
