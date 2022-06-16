# -*- coding: utf-8 -*-
"""
https://leetcode.cn/problems/k-diff-pairs-in-an-array/

给你一个整数数组 nums 和一个整数 k，请你在数组中找出 不同的 k-diff 数对，并返回不同的 k-diff 数对 的数目。

k-diff 数对定义为一个整数对 (nums[i], nums[j]) ，并满足下述全部条件：

- 0 <= i, j < nums.length
- i != j
- |nums[i] - nums[j]| == k
注意，|val| 表示 val 的绝对值。
"""

import collections
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """
        题意可简化为在一个无序数组nums中找不重复组合数对，组合的条件是二者之差为k。
        
        1. 数组的顺序不重要，可以排序
        2. 因为求的是不重复的组合数对，所以数组理论上可以简化为集合
        3. 考虑0-diff数对，这种情况需要保证数组元素重复出现两次以上，因此元素次数信息需要保存
        4. 构造一个字典计数器，记录nums中每个元素出现的次数
        5. 从小到大遍历计数器的每个num，进行检测：
            - 若 k = 0, 则num出现次数大于等于2即可
            - 若 k > 0, 则num + k存在即可
            如此遍历可覆盖全部可能的组合数对
        """
        ans = 0
        counter = collections.Counter(nums)
        for n in sorted(counter.keys()):
            if k == 0:
                if counter[n] > 1:
                    ans += 1
            else:
                if n + k in counter:
                    ans += 1
        return ans


class Solution2:
    def findPairs(self, nums: List[int], k: int) -> int:
        """
        思路同解法一，只是统一了k的检测逻辑
        """
        ans = 0
        counter = collections.Counter(nums)
        min_cnt = 2 if k == 0 else 1
        for n in sorted(counter.keys()):
            if n + k in counter and counter[n + k] >= min_cnt:
                ans += 1
        return ans