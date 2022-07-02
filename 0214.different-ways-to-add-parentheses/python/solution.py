# -*- coding: utf-8 -*-

"""
https://leetcode.cn/problems/different-ways-to-add-parentheses

给你一个由数字和运算符组成的字符串 expression ，按不同优先级组合数字和运算符，计算并返回所有可能组合的结果。你可以 按任意顺序 返回答案。

生成的测试用例满足其对应输出值符合 32 位整数范围，不同结果的数量不超过 104 。

"""

import operator
from typing import List
import functools


class Solution:
    """
    没做出来。
    参考答案：https://leetcode.cn/problems/different-ways-to-add-parentheses/solution/pythongolang-fen-zhi-suan-fa-by-jalan/
    """
    @functools.lru_cache(maxsize=None)
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # 如果只有数字，直接返回
        if expression.isdigit():
            return [int(expression)]

        res = []
        for i, char in enumerate(expression):
            if char in ['+', '-', '*']:
                # 1.分解：遇到运算符，计算左右两侧的结果集
                # 2.解决：diffWaysToCompute 递归函数求出子问题的解
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                # 3.合并：根据运算符合并子问题的解
                for l in left:  # noqa
                    for r in right:
                        if char == '+':
                            res.append(l + r)
                        elif char == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)

        return res


class Solution1:
    """
    自底向上的区间dp算法
    参考答案：https://leetcode.cn/problems/different-ways-to-add-parentheses/solution/wei-yun-suan-biao-da-shi-she-by-jiang-hu-0pf0/
    """
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # 转换表达式
        ops = []

        i = 0
        n = len(expression)

        while i < n:
            if expression[i] in "+-*":
                ops.append(expression[i])
                i += 1
            else:
                num = 0
                while i < n and expression[i].isdigit():
                    num = num * 10 + int(expression[i])
                    i += 1
                ops.append(num)

        # 构造dp，dp[i][j]表示ops[i]到ops[j]表达式所有可能的解
        n = len(ops)
        dp = [[[] for _ in range(n)] for _ in range(n)]

        # 计算区间=1的解
        for i in range(0, n, 2):
            dp[i][i].append(ops[i])

        # 计算区间=3,5...的子问题的解，逐步到n
        for length in range(3, n + 1, 2):
            for left in range(0, n - length + 1, 2):
                right = left + length - 1
                for i in range(left + 1, right, 2):
                    dp[left][right].extend(self.merge(ops[i], dp[left][i - 1], dp[i + 1][right]))

        return dp[0][n - 1]

    def merge(self, op: str, lefts: List[int], rights: List[int]):
        """ 合并结果 """
        if op == "+":
            f = operator.add
        elif op == "-":
            f = operator.sub
        elif op == "*":
            f = operator.mul
        else:
            raise ValueError(f"invalid op: {op}")

        ret = []
        for le in lefts:
            for ri in rights:
                ret.append(f(le, ri))

        return ret


if __name__ == "__main__":
    s = Solution1()
    ret = s.diffWaysToCompute("12*3-64*75")
    print(ret)
