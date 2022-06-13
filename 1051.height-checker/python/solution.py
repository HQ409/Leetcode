# -*- coding: utf-8 -*-
"""
https://leetcode.cn/problems/height-checker/

1. 排序后，与原数组比较
2. 因为高度有界，可以使用数组计数（index为高度值，value为出现次数），然后遍历计数数组和原数组，可以把复杂度降到O(n)
"""

from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        return (sum(1 for x, y in zip(expected, heights) if x != y))


class Solution2:
    def heightChecker(self, heights: List[int]) -> int:
        # 纪录每个height出现的次数
        m = max(heights)
        cnt = [0] * (m + 1)

        for h in heights:
            cnt[h] += 1

        # idx为heights数组下标
        # ans为高度不一致的计数
        idx = ans = 0
        # 遍历计数数组
        for i in range(1, m + 1):
            # 只处理值>0的下标，此时的下标i应当为heights数组在idx下标之后最小的值
            for _ in range(cnt[i]):
                if heights[idx] != i:
                    ans += 1
                idx += 1

        return ans