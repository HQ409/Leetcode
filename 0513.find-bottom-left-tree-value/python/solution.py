# -*- coding: utf-8 -*-
"""
https://leetcode.cn/problems/find-bottom-left-tree-value/

给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。

假设二叉树中至少有一个节点。
"""
from typing import Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        """
        BFS，每个层级从右往左遍历
        """
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
            ans = node.val
        return ans


class Solution2:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        """
        BFS，每个层级从右往左遍历，使用双端队列替换list
        """
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
            ans = node.val
        return ans
