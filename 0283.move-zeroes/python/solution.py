# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/move-zeroes/

p代表处理好的数组位置，q遍历数组，遇到非0和p交换。交换有两种情况：
(1) nums[p]==0, nums[q]!=0
(2) nums[p]==nums[q]!=0,原地拷贝

另外一种比较好理解思路是，遍历非0的元素往数组头部填充，然后对数组尾部补0。
https://leetcode-cn.com/problems/move-zeroes/solution/dong-hua-yan-shi-283yi-dong-ling-by-wang_ni_ma/
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p, n = 0, len(nums)
        for q in range(n):
            if nums[q] != 0:
                nums[p], nums[q] = nums[q], nums[p]
                p += 1