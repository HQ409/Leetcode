"""
https://leetcode.cn/problems/minimum-absolute-difference/

给你个整数数组 arr，其中每个元素都 不相同。

请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。

"""
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        """
        排序 + 一次遍历
        """
        arr.sort()
        min_abs = arr[-1] - arr[0]
        ret = []
        for i in range(len(arr) - 1):
            abs = arr[i + 1] - arr[i]
            if abs < min_abs:
                min_abs = abs
                ret = [[arr[i], arr[i + 1]]]
            elif abs == min_abs:
                ret.append([arr[i], arr[i + 1]])
        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]))
