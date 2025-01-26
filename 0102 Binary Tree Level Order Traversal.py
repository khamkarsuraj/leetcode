# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs
        # time n
        # space w where w is width of the tree
        if not root:
            return  []

        q = deque([root])
        ans = []

        while q:
            temp = []

            for i in range(0, len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                temp.append(node.val)

            ans.append(temp)

        return ans
