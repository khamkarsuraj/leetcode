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
    //Time: O(n)
    //Space: O(1)
    public int depth(TreeNode currentNode) {
        if (currentNode == null) return 0;

        return Math.max(depth(currentNode.left), depth(currentNode.right)) + 1;
    }

    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        
        return this.depth(root);
    }
}
