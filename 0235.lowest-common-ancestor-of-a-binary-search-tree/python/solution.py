# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 处于两个子树
        if p.val <= root.val <= q.val or p.val >= root.val >= q.val:
            return root
        if p.val <= root.val and q.val <= root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val >= root.val and q.val >= root.val:
            return self.lowestCommonAncestor(root.right, p, q)