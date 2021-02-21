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
class FindElements {
    
    public Set<Integer> s = new HashSet<Integer>();
    public FindElements(TreeNode root) {
        setVal(root, 0);
    }
    
    public void setVal(TreeNode node, int val) {
        if(node == null)    return;
        node.val = val;
        s.add(val);
        this.setVal(node.left, 2*val+1);
        this.setVal(node.right, 2*val+2);
    }
    
    public boolean find(int target) {
        return s.contains(target);
    }
}
