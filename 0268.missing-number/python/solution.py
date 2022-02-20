# -*- coding: utf-8 -*-
"""
268. 丢失的数字
https://leetcode-cn.com/problems/missing-number/
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        return total - sum(nums)