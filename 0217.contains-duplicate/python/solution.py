# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for n in nums:
            if n not in counter:
                counter[n] = 1
            else:
                return True
        return False