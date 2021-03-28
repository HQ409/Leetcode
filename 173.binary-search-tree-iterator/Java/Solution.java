package Java;

/**
 * @see <a href="https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/"></a>
 * 83. 删除排序链表中的重复元素
 * 未完成
 */
class BSTIterator {
    TreeNode fakeRoot = new TreeNode(0);
    TreeNode farRightNode = fakeRoot;
    TreeNode currentNode;

    public BSTIterator(TreeNode root) {
        //将root从树变成链表
        inOrder(root);

        currentNode = fakeRoot.right;
    }

    void inOrder(TreeNode treeNode) {
        if (treeNode != null) {
            inOrder(treeNode.left);
            farRightNode.right = treeNode;
            farRightNode = treeNode;
            inOrder(treeNode.right);
            farRightNode.right = null;
        }
    }

    public int next() {
        int val = currentNode.val;
        currentNode = currentNode.right;
        return val;
    }

    public boolean hasNext() {
        return currentNode != null;
    }

    public static void main(String[] s) throws Exception {
        TreeNode treeNode1 = new TreeNode(7);
        TreeNode treeNode2 = new TreeNode(3);
        TreeNode treeNode3 = new TreeNode(15);
        TreeNode treeNode4 = new TreeNode(9);
        TreeNode treeNode5 = new TreeNode(20);
        treeNode1.left = treeNode2;
        treeNode1.right = treeNode3;
        treeNode3.left = treeNode4;
        treeNode3.right = treeNode5;
        BSTIterator BSTIterator = new BSTIterator(treeNode1);
        System.out.println(BSTIterator.next());
        System.out.println(BSTIterator.next());
        System.out.println(BSTIterator.hasNext());
        System.out.println(BSTIterator.next());
        System.out.println(BSTIterator.hasNext());
        System.out.println(BSTIterator.next());
        System.out.println(BSTIterator.hasNext());
        System.out.println(BSTIterator.next());
        System.out.println(BSTIterator.hasNext());
    }
}


class TreeNode {
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

    @Override
    public String toString() {
        final StringBuffer sb = new StringBuffer("<");
        sb.append(val).append(">");
        return sb.toString();
    }
}


