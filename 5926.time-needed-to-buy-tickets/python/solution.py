# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        seconds = 0
        while tickets[k] != 0:
            t = tickets.pop(0)
            if t > 0:
                tickets.append(t - 1)
                seconds += 1
            k = (k - 1) % len(tickets)
        return seconds