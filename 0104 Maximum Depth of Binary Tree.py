# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursion
        # time n
        # space h where h is height of the tree
        '''
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        '''

        # iterative - BFS
        # time n
        # space n
        if not root:
            return 0

        depth = 0
        que = deque([root])

        while que:
            depth += 1
            for _ in range(len(que)):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

        return depth


        
