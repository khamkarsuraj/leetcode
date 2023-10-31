# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Using Depth First Search Algorithm
    # Time: O(n)
    # Space: O(h) where h is height of tree heighest tree between root and subRoot
    
    # 4. Once you are here. You have found one common node, check for all childs
    def dfs(self, current, subRoot):
        # 5. If you reached till bottom of both current and subRoot and haven't return False yet
        # It means that whatever the path you came through is identical, so return True
        if (current == None and subRoot == None):
            return True
        # If any of the tree is finished before another tree
        # there are difference between no of nodes, return False
        elif (current == None or subRoot == None):
            return False
        
        # 6. If node exists but value is different for nodes, return False
        if (current.val != subRoot.val):
            return False
        # Else, values are same then go for remaining nodes
        else:
            return self.dfs(current.left, subRoot.left) and self.dfs(current.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 2. If reached to bottom of tree and still not found common node, return False
        if (root == None):
            return False
        
        # 3. When you found common node, go and check its remaining nodes as well.
        # If found all nodes same, return true
        # else check if is there any other common node exists using 1.
        if (self.dfs(root, subRoot)):
            return True
        
        # 1. Keep checking for first common node between root and subRoot if is there any
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
