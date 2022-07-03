"""
https://leetcode.cn/problems/minimum-number-of-refueling-stops

根据Leetcode.871改编的题目，难度其实是一样的，只是为了避免面试人背题AC。

修改如下：

汽车从起点出发驶向目的地，该目的地位于出发位置东面 target 英里处。

沿途有加油站，每个 station[i] 代表一个加油站，它位于出发位置东面 station[i][0] 英里处，并且有 station[i][1] 升汽油，每升汽油价格为station[i][2]元。

假设汽车油箱的容量是无限的，其中最初有 startFuel 升燃料。它每行驶 1 英里就会用掉 1 升汽油。

当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中。

为了到达目的地，汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 -1 。

注意：如果汽车到达加油站时剩余燃料为 0，它仍然可以在那里加油。如果汽车到达目的地时剩余燃料为 0，仍然认为它已经到达目的地。
"""
from typing import List
import heapq


class Solution:
    """
    贪心 + 堆
    """
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """
        贪心策略：默认不加油，直到无法到达下一个加油站或者终点时，再从经过的加油站中选择油量最多的加油。
        用堆实现选取最大油量的加油站，降低时间复杂度
        """
        cost = 0
        stations.append([target, 0, 0])
        visited_stations = []
        for pos, fuel, price in stations:
            while startFuel < pos:
                if len(visited_stations) == 0:
                    return -1
                lowprice, cheapfuel = heapq.heappop(visited_stations)
                needfuel = pos - startFuel
                if needfuel > cheapfuel:
                    startFuel += cheapfuel
                    cost += lowprice * cheapfuel
                    print("加油：{}L, 单价格：{}元，总价：{}元".format(cheapfuel, lowprice, lowprice * cheapfuel))
                else:
                    startFuel += needfuel
                    cost += lowprice * needfuel
                    print("加油：{}L, 单价格：{}元，总价：{}元".format(needfuel, lowprice, lowprice * needfuel))
                    heapq.heappush(visited_stations, (lowprice, cheapfuel - needfuel))
            heapq.heappush(visited_stations, (price, fuel))
        return cost


if __name__ == "__main__":
    s = Solution()
    target = 100
    startFuel = 20
    stations = [[10, 60, 20], [20, 30, 25], [30, 30, 15], [60, 40, 10]]
    ret = s.minRefuelStops(target, startFuel, stations)
    print(ret)