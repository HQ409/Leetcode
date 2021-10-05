# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indexes = {}
        for i, n in enumerate(nums):
            if n in indexes:
                distance = i - indexes[n]
                if distance <= k:
                    return True
            indexes[n] = i
        return False


if __name__ == "__main__":
    s = Solution()
    ret = s.containsNearbyDuplicate([1, 0, 1, 1], 1)
    print(ret)