package Java;

import java.util.ArrayList;
import java.util.List;

/**
 * @see <a href="https://leetcode-cn.com/problems/binary-tree-inorder-traversal/"></a>
 */
class Solution0094 {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> resultList = new ArrayList<>();
        traversal(root, resultList);
        return resultList;
    }

    public void traversal(TreeNode root, List<Integer> resultList) {
        if (root != null) {
            traversal(root.left, resultList);
            resultList.add(root.val);
            traversal(root.right, resultList);
        }
    }

    static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
}