/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    //Recursion
    //Time: O(n) n is no of nodes
    //Space: O(1)
    public boolean helper(TreeNode currentP, TreeNode currentQ) {
        //If you reached to last nodes, and both have null values. tree is identical so far
        if (currentP == null && currentQ == null) return true;

        //If any of the two nodes are null
        //OR if both are not null and have different values trees are not identical
        if (currentP == null || currentQ == null || currentP.val != currentQ.val) return false;

        //Still, if you reached here, go to left or right of both trees at the sam time
        //to compare next elements
        return helper(currentP.left, currentQ.left) && helper(currentP.right, currentQ.right);
    }

    public boolean isSameTree(TreeNode p, TreeNode q) {
        return this.helper(p, q);
    }
}
