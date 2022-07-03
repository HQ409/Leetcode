"""
https://leetcode.cn/problems/minimum-number-of-refueling-stops

汽车从起点出发驶向目的地，该目的地位于出发位置东面 target 英里处。

沿途有加油站，每个 station[i] 代表一个加油站，它位于出发位置东面 station[i][0] 英里处，并且有 station[i][1] 升汽油。

假设汽车油箱的容量是无限的，其中最初有 startFuel 升燃料。它每行驶 1 英里就会用掉 1 升汽油。

当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中。

为了到达目的地，汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 -1 。

注意：如果汽车到达加油站时剩余燃料为 0，它仍然可以在那里加油。如果汽车到达目的地时剩余燃料为 0，仍然认为它已经到达目的地。
"""
import time
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
        cnt = 0
        stations.append([target, 0])
        visited_stations = []
        for pos, fuel in stations:
            while startFuel < pos:
                if len(visited_stations) == 0:
                    return -1
                maxfuel = -heapq.heappop(visited_stations)
                startFuel += maxfuel
                cnt += 1
            heapq.heappush(visited_stations, -fuel)
        return cnt


class Solution3:
    """
    贪心算法
    """
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """
        贪心策略：默认不加油，直到无法到达下一个加油站或者终点时，再从经过的加油站中选择油量最多的加油。
        """
        cnt = 0
        stations.append([target, 0])
        visited_stations = []
        for pos, fuel in stations:
            while startFuel < pos:
                if len(visited_stations) == 0:
                    return -1
                maxfuel = max(visited_stations)
                cnt += 1
                visited_stations.remove(maxfuel)
                startFuel += maxfuel
            visited_stations.append(fuel)
        return cnt


class Solution2:
    """
    根据Solution1，优化plan空间，相同加油次数只记录剩油最多的结果
    """
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # 记plan为到达当前加油站所有可能的方案
        # kye=加油次数，value=剩余油量
        plan = {0: startFuel}
        # pos=汽车当前位置
        pos = 0
        for station in stations:
            next_plan = {}
            dis = station[0] - pos
            for times, fuel in plan.items():
                if fuel >= dis:
                    if times in next_plan:
                        next_plan[times] = max(next_plan[times], fuel - dis)
                    else:
                        next_plan[times] = fuel - dis

                    if times + 1 in next_plan:
                        next_plan[times + 1] = max(next_plan[times], fuel - dis + station[1])
                    else:
                        next_plan[times + 1] = fuel - dis + station[1]

            if len(next_plan) == 0:
                return -1

            pos = station[0]
            plan = next_plan

        ret = -1
        for times, fuel in plan.items():
            if fuel >= target - pos and (ret == -1 or times < ret):
                ret = times
        return ret


class Solution1:
    """
    穷举所有方法，超时
    """
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # 记plans为到达当前加油站所有可能的方案
        # plan[0]=加油次数，plan[1]=剩余油量
        plans = [(0, startFuel)]
        # pos=汽车当前位置
        pos = 0
        for station in stations:
            print(plans)
            print("time: {}, station: {}, plains: {}".format(time.strftime("%Y-%m-%d %H:%M:%S"), station, len(plans)))
            last_plains = plans
            plans = []
            dis = station[0] - pos
            for plan in last_plains:
                if plan[1] >= dis:
                    plan0 = (plan[0], plan[1] - dis)                    # 不在这个加油站加油
                    plan1 = (plan[0] + 1, plan[1] - dis + station[1])   # 在这个加油站加油
                    plans.append(plan0)
                    plans.append(plan1)
            if len(plans) == 0:
                return -1
            pos = station[0]

        ret = -1
        dis = target - pos
        for plan in plans:
            if plan[1] >= dis and (ret == -1 or plan[0] < ret):
                ret = plan[0]
        return ret


if __name__ == "__main__":
    s = Solution()
    target = 1000
    startFuel = 1
    stations = [[1, 186], [145, 161], [183, 43], [235, 196], [255, 169], [263, 200], [353, 161], [384, 190], [474, 44],
                [486, 43], [567, 48], [568, 96], [592, 36], [634, 181], [645, 167], [646, 69], [690, 52], [732, 28],
                [800, 42], [857, 55], [922, 63], [960, 141], [973, 13], [977, 112], [997, 162]]
    ret = s.minRefuelStops(target, startFuel, stations)
    print(ret)