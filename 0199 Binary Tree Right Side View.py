class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs 
        # time n
        # space w
        if not root:
            return []
        
        q = deque([root])
        ans = []

        while q:
            l = len(q)
            for i in range(0, l):
                # missed this logic
                # added two loops one for adding childs and another for removing popleft
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
    
            ans.append(node.val)

        return ans


# class Solution:
#     def rightSideView(self, root: TreeNode) -> int:
#         # dfs
#         # time n
#         # space h
#         ans = []

#         def dfs(node, depth):
#             if not node:
#                 return
            
#             # If visiting this depth for the first time, add the node's value
#             if depth == len(ans):
#                 ans.append(node.val)
            
#             # Visit the right child first, then the left child
#             dfs(node.right, depth + 1)
#             dfs(node.left, depth + 1)
        
#         dfs(root, 0)
#         return ans
