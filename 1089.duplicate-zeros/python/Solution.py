# -*- coding: utf-8 -*-
"""
https://leetcode.cn/problems/duplicate-zeros

给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。
注意：请不要在超过该数组长度的位置写入元素。
要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。


示例 1：

输入：[1,0,2,3,0,4,5,0]
输出：null
解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]
示例 2：

输入：[1,2,3]
输出：null
解释：调用函数后，输入的数组将被修改为：[1,2,3]
 

提示：
1 <= arr.length <= 10000
0 <= arr[i] <= 9

"""

from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        循环插入，最后删除
        """
        i, lenght = 0, len(arr)
        while i < lenght:
            if arr[i] == 0:
                arr.insert(i, 0)
                i += 2
            else:
                i += 1
        del arr[lenght:]


class Solution2:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        边插边删
        """
        i, lenght = 0, len(arr)
        while i < lenght:
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 2
            else:
                i += 1


class Solution3:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        不用insert
        非0元素移动的距离取决于元素左边0的个数
        """
        arrlen, cnt0 = len(arr), arr.count(0)
        # 从右往左处理，维护变量cnt0=当前元素左边的0的个数，计算元素往右平移后的下标，超过arrlen-1丢弃
        i = arrlen - 1
        while i >= 0:
            # 先计算cnt0
            if arr[i] == 0:
                # 减去当前元素0
                cnt0 -= 1
                # 如果没有超过数组长度，则额外复写一个0
                if i + cnt0 + 1 < arrlen:
                    arr[i + cnt0 + 1] = 0 
            # 元素右移
            if i + cnt0 < arrlen:
                arr[i + cnt0] = arr[i]
            i -= 1


class Solution4:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        不用insert，用双指针实现一个类似栈的效果，还是蛮巧妙的：
        https://leetcode.cn/problems/duplicate-zeros/solution/fu-xie-ling-by-leetcode-solution-7ael/
        """
        n = len(arr)
        top = 0
        i = -1
        while top < n:
            i += 1
            top += 1 if arr[i] else 2
        j = n - 1
        if top == n + 1:
            arr[j] = 0
            j -= 1
            i -= 1
        while j >= 0:
            arr[j] = arr[i]
            j -= 1
            if arr[i] == 0:
                arr[j] = arr[i]
                j -= 1
            i -= 1


if __name__ == "__main__":
    solution = Solution3()
    nums = [1, 0, 2, 3, 0, 4, 5, 0]
    solution.duplicateZeros(nums)
    print(nums)