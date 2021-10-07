# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        
        ret = []
        end = start = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[start] == i - start:
                end = i
            else:
                if end == start:
                    ret.append(f"{nums[start]}")
                else:
                    ret.append(f"{nums[start]}->{nums[end]}")
                end = start = i

        if end == start:
            ret.append(f"{nums[start]}")
        else:
            ret.append(f"{nums[start]}->{nums[end]}")

        return ret
