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
    public void swap(TreeNode currentNode) {
        if (currentNode == null) return;

        TreeNode temp = currentNode.left;
        currentNode.left = currentNode.right;
        currentNode.right = temp;

        swap(currentNode.left);
        swap(currentNode.right);
    }

    public TreeNode invertTree(TreeNode root) {
        if (root == null) return root;

        this.swap(root);
        return root;
    }
}
