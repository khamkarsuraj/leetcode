class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs - recursion
        # time n
        # space h
        if not root:
            return True

        def dfs(root):
            if not root:
                return 0

            lh = dfs(root.left)
            rh = dfs(root.right)

            if abs(lh - rh) > 1 or lh == -1 or rh == -1:
                return -1
            return 1 + max(lh, rh)
        
        if dfs(root) == -1:
            return False
        return True
