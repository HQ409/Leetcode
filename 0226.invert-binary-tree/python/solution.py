# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 递归：自下而上
        if root is None:
            return root

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    def invertTree2(self, root: TreeNode) -> TreeNode:
        # 迭代：前序遍历（中左右）
        stack = []
        if root:
            stack.append(root)
        while len(stack) > 0:
            cur = stack.pop()
            cur.left, cur.right = cur.right, cur.left   # 中
            if cur.right:                               # 右
                stack.append(cur.right)
            if cur.left:                                # 左
                stack.append(cur.left)
        return root