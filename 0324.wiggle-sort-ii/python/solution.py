"""
https://leetcode.cn/problems/wiggle-sort-ii

给你一个整数数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。

你可以假设所有输入数组都可以得到满足题目要求的结果。

"""
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        参考解法一：https://leetcode.cn/problems/wiggle-sort-ii/solution/yi-bu-yi-bu-jiang-shi-jian-fu-za-du-cong-onlognjia/
        时间复杂度：O(nlogn)
        空间复杂度：O(n)

        这个题的进阶做法相当有难度，可以参考链接的其他解法和官方题解说明：
        https://leetcode.cn/problems/wiggle-sort-ii/solution/bai-dong-pai-xu-ii-by-leetcode-solution-no0s/
        """
        if len(nums) < 2:
            return None

        # 排序后分成两部分，然后从两部分由大到小取数（避免重复数相邻）
        sorted_nums = sorted(nums)
        right = len(nums) - 1       # 较大元素的最右下标
        left = right // 2           # 较小元素的最右下标

        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = sorted_nums[left]
                left -= 1
            else:
                nums[i] = sorted_nums[right]
                right -= 1


if __name__ == "__main__":
    s = Solution()
    # nums = [1,5,1,1,6,4]
    nums = [1, 3, 2, 2, 3, 1]
    s.wiggleSort(nums)
    print(nums)
