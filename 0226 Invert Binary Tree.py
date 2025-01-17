# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # iterative - bfs
        # time n
        # space n
        if not root:
            return None
        
        queue = deque([root])  # Initialize a queue with the root node
        
        while queue:
            node = queue.popleft()  # Get the next node from the queue
            
            # Swap the left and right children
            node.left, node.right = node.right, node.left
            
            # Add the children to the queue if they exist
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root

        # recursion
        # time n
        # space h
        # while not root:
        #     return
        
        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # root.left, root.right = root.right, root.left

        # return root
