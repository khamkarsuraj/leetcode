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
    //Using Depth First Search Algorithm
    //Time: O(n)
    //Space: O(h) where h is height of tree heighest tree between root and subRoot

    // 4. Once you are here. You have found one common node, check for all childs
    public boolean dfs(TreeNode root, TreeNode subRoot) {
        // 5. If you reached till bottom of both current and subRoot and haven't return False yet
        // It means that whatever the path you came through is identical, so return True
        if (root == null && subRoot == null) return true;

        // If any of the tree is finished before another tree
        // there are difference between no of nodes, return False
        else if (root == null || subRoot == null) return false;

        // 6. If node exists but value is different for nodes, return False
        if (root.val != subRoot.val) return false;
        // Else, values are same then go for remaining nodes
        else return (dfs(root.left, subRoot.left) && dfs(root.right, subRoot.right));
    }

    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        // 2. If reached to bottom of tree and still not found common node, return False
        if (root == null) return false;
        
        // 3. When you found common node, go and check its remaining nodes as well.
        // If found all nodes same, return true
        // else check if is there any other common node exists using 1.
        if (this.dfs(root, subRoot)) return true;
        
        //1. Keep checking for first common node between root and subRoot if is there any
        return (isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot));
    }
}
