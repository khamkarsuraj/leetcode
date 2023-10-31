/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    // Using DFS: Recursion
    // Time: O(n) n - no of nodes in longest path
    // Space: O(h) h - maximum height of the tree
  
    public TreeNode dfs(TreeNode root, TreeNode p, TreeNode q) {
      // Try finding common ancestor for p and q.
      // You have to go eighter left or right from current node
      // If p and q splits to two different sides then that's your common ancestor, simply return it
      // else keep going to left or right
      if (p.val < root.val && q.val < root.val) return dfs(root.left, p, q);
      else if (p.val > root.val && q.val > root.val) return dfs(root.right, p, q);
      
      return root;
    }

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        return this.dfs(root, p, q);
    }
}
