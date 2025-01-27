class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs
        # time n
        # space h
        ans = 0

        def dfs(max_val, curr):
            if not curr:
                return
            
            nonlocal ans
            if curr.val >= max_val:
                max_val = curr.val
                ans += 1

            dfs(max_val, curr.left)
            dfs(max_val, curr.right)
        
        dfs(root.val, root)

        return ans
