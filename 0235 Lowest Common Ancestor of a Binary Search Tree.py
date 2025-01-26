class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # bfs leveraging BST
        # time h
        # space 1

        while True:
            # check where to go left or right
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            # if no where to, it does mean that p and q splits here which is LCA
            else:
                break

        return root
