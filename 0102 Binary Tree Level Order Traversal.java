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
    public List<List<Integer>> levelOrder(TreeNode root) {
        //BFS - using queue
        //Time: O(n) where n is no of nodes in tree
        //Space: O(m) where maximum nodes in any level
        List<List<Integer>> final_lists = new ArrayList<List<Integer>>();
    
        if (root == null) {
           return final_lists;
        }

        Queue<TreeNode> queue = new LinkedList<>();

        queue.add(root);

        while (!queue.isEmpty()) {
            List<Integer> list = new LinkedList<>();
            int level = queue.size();
            for(int i=0; i<level; i++){
                if(queue.peek().left != null) queue.add(queue.peek().left);
                if(queue.peek().right != null) queue.add(queue.peek().right);
                list.add(queue.peek().val);
                queue.remove();
            }
            final_lists.add(list);
        }

        return final_lists;
    }
}
