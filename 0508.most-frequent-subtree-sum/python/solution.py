"""
https://leetcode.cn/problems/most-frequent-subtree-sum/

给你一个二叉树的根结点 root ，请返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。

一个结点的 「子树元素和」 定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。
"""
import collections
import functools
from typing import List


# Definition for a Node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        cnt = collections.Counter()
        # 记录每个节点的子树元素和
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            cnt[self.treesum(node)] += 1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        # 找到出现次数最多的值
        max_occurs = max(cnt.values())
        return [k for k, v in cnt.items() if v == max_occurs]

    @functools.lru_cache()
    def treesum(self, root: TreeNode) -> int:
        """
        递归计算节点元素和，缓存中间结果
        """
        if not root:
            return None

        ret = root.val
        lsum = self.treesum(root.left)
        if lsum is not None:
            ret += lsum
        rsum = self.treesum(root.right)
        if rsum is not None:
            ret += rsum

        return ret


class Solution2:
    """
    解法一其实对树重复遍历了，直接一次DFS就行了，动图演示：
    https://leetcode.cn/problems/most-frequent-subtree-sum/solution/by-jiang-hui-4-rw8g/
    """
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        cnt = collections.Counter()

        def treesum(node: TreeNode) -> int:
            """
            DFS递归计算子树元素和
            """
            if node is None:
                return 0

            ret = node.val + treesum(node.left) + treesum(node.right)
            cnt[ret] += 1
            return ret

        treesum(root)
        max_occurs = max(cnt.values())
        return [k for k, v in cnt.items() if v == max_occurs]


if __name__ == "__main__":
    pass
