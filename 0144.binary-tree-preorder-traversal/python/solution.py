# -*- coding: utf-8 -*-

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    先序遍历：根节点-》左子树-》右子树
    """
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        # 迭代遍历
        if root is None:
            return []

        # 保证stack中的节点都不是空节点
        stack = [root]
        ret = []

        while len(stack) > 0:
            cur = stack.pop()
            ret.append(cur.val)
            if cur.right is not None:
                stack.append(cur.right)
            if cur.left is not None:
                stack.append(cur.left)

        return ret


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    s = Solution()
    ret = s.preorderTraversal2(root)
    print(ret)