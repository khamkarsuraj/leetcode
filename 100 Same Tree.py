# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Recursion
    #Time: O(n) n is no of nodes
    #Space: O(1)
    def helper(self, currentP, currentQ):
        #If you reached to last nodes, and both have null values. tree is identical so far
        if (currentP == None and currentQ == None):
            return True

        #If any of the two nodes are null
        #OR if both are not null and have different values trees are not identical
        if (currentP == None or currentQ == None or currentP.val != currentQ.val):
            return False

        #Still, if you reached here, go to left or right of both trees at the sam time
        #to compare next elements
        return self.helper(currentP.left, currentQ.left) and self.helper(currentP.right, currentQ.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.helper(p, q) 
