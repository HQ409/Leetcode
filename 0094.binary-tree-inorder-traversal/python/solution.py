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
    中序遍历：左子树-》根节点-》右子树
    """
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归遍历
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        # 迭代遍历
        cur = root
        stack = []
        ret = []
        while 1:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            elif len(stack) > 0:
                cur = stack.pop()
                ret.append(cur.val)
                cur = cur.right
            else:
                break
        return ret


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    s = Solution()
    ret = s.inorderTraversal2(root)
    print(ret)