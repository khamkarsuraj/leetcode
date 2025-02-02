class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # dfs - Inorder traversal
        # time n
        # space h
        ranking = 0
        ans = None

        def dfs(root):
            nonlocal ranking, ans
            if not root or ans is not None:
                return # return earlier if found ans already

            dfs(root.left)

            ranking += 1 # rank current node

            if ranking == k:
                ans = root.val
                return # return earlier if found ans

            dfs(root.right)

        dfs(root)
        return ans
