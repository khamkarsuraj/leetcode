class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # dfs
        # time n
        # space h
        maxSum = float('-inf')

        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0
            
            # ignore negative node values
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # compute the maximum path sum including both branches
            maxSum = max(maxSum, left + right + node.val)

            # return the best sum that can be extended to the parent
            # can not extend both branches upwards to parent
            return node.val + max(left, right)

        dfs(root)
        return maxSum
