# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Recursion
    #Time: O(n)
    #Space: O(1)
    def swap(self, currentNode):
        if (currentNode == None):
            return

        temp = currentNode.left
        currentNode.left = currentNode.right
        currentNode.right = temp

        self.swap(currentNode.left)
        self.swap(currentNode.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if (root == None):
            return root

        self.swap(root)
        return root        
