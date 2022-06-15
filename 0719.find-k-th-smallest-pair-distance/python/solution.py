# -*- coding: utf-8 -*-
"""
https://leetcode.cn/problems/find-k-th-smallest-pair-distance/
"""

# import heapq
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """
        1. 距离取绝对值，所以数组元素相对顺序不重要（可以自己用手模拟一下，其实就是任意两个数对）
        2. O(n2)用什么方法优化都timeout，因此必须降低时间复杂度，O(n)显然是不可能的，所以我们考虑O(nlogn)，这个复杂度最常见的就是二分
        3. 二分的思路比较特别，大致上来说：
            left = 最小距离，right = 最大距离，mid = (left + right) / 2
            记target=距离<mid的数对，即mid是第target小的距离
                如果target>=k，下一步right=mid
                如果target<k，下一步left=mid+1
            详细的二分边界查看：https://leetcode.cn/problems/find-k-th-smallest-pair-distance/solution/er-fen-cha-zhao-hua-dong-chuang-kou-java-8q95/
        4. 计算距离<mid的数对方法比较好理解的是双指针：
            https://leetcode.cn/problems/find-k-th-smallest-pair-distance/solution/-by-xiaohu9527-ioe6/
        5. 全部理解清楚之后，再阅读宫水三叶的题解：
            https://leetcode.cn/problems/find-k-th-smallest-pair-distance/solution/by-ac_oier-o4if/
        """
        def count(mid: int) -> int:
            cnt = i = 0
            for j, num in enumerate(nums):
                while num - nums[i] > mid:
                    i += 1
                cnt += j - i
            return cnt

        nums.sort()
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + right >> 1
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return right


class Solution_TIMEOUT:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """ O(n2)遍历 + 桶排序，超时 """
        max_distance = max(nums)
        buckets = [0] * (max_distance + 1)
        for i, n in enumerate(nums):
            for m in nums[i + 1:]:
                distance = abs(m - n)
                buckets[distance] += 1

        for bucket, cnt in enumerate(buckets):
            if cnt == 0:
                continue
            k -= cnt
            if k <= 0:
                return bucket


if __name__ == "__main__":
    import os
    import json
    import traceback
    import time

    CURDIR = os.path.dirname(os.path.abspath(__file__))
    test_data_file = os.path.join(CURDIR, "test_data.json")
    test_data = json.load(open(test_data_file))
    s = Solution()
    for item in test_data:
        if not item["active"]:
            continue
        t = time.clock()
        try:
            ret = s.smallestDistancePair(**item["args"])
            if "ret" in item and ret != item["ret"]:
                print("fail!!args={}, ret={}, required={}".format(item["args"], ret, item["ret"]))
            else:
                print("success!!args={}, ret={}".format(item["args"], ret))
        except Exception:
            print("exception!!args={}".format(item["args"]))
            traceback.print_exc()
        finally:
            print("time cost: {}s".format(time.clock() - t))