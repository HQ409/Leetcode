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
    后序遍历：左子树-》右子树-》根节点
    """
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归遍历
        if root is None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        # 迭代遍历
        ret = []
        stack = []
        cur = root
        prev = None

        while 1:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            elif len(stack) > 0:
                cur = stack.pop()
                if cur.right is None or cur.right == prev:
                    # 右子树已遍历完毕
                    ret.append(cur.val)
                    prev = cur
                    cur = None
                else:
                    stack.append(cur)
                    cur = cur.right
            else:
                break

        return ret

    def postorderTraversal3(self, root: TreeNode) -> List[int]:
        # 迭代遍历: 不借助prev变量，未完成
        ret = []
        stack = []
        cur = root

        while 1:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            elif len(stack) > 0:
                cur = stack.pop()
                if cur.left is None and cur.right is None:
                    ret.append(cur.val)
                if cur.right is not None:
                    stack.append(cur.right)
                if cur.left is not None:
                    stack.append(cur.left)
                cur = None
            else:
                break

        return ret


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    s = Solution()
    ret = s.postorderTraversal3(root)
    print(ret)