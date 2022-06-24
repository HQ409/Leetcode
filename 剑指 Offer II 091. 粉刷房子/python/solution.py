"""
https://leetcode.cn/problems/JEj789

假如有一排房子，共 n 个，每个房子可以被粉刷成红色、蓝色或者绿色这三种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。

当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x 3 的正整数矩阵 costs 来表示的。

例如，costs[0][0] 表示第 0 号房子粉刷成红色的成本花费；costs[1][2] 表示第 1 号房子粉刷成绿色的花费，以此类推。

请计算出粉刷完所有房子最少的花费成本。

"""
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        时间复杂度：O(n)
        空间复杂度：O(1), 三个局部变量 + 一个定长min_cost数组
        """
        min_cost = costs[0]
        # 记最后一个房子为红色的最小成本为min_cost[0]
        # 记最后一个房子为蓝色的最小成本为min_cost[1]
        # 记最后一个房子为绿色的最小成本为min_cost[2]
        # 遍历计算min_cost
        for i in range(1, len(costs)):
            cost = costs[i]
            # 最后一个房子为红色的最小成本：该房子单独粉刷成红色的成本 + 上一个房子不是红色的最小成本之和
            # 其他颜色也是一样的
            min_cost0 = cost[0] + min(min_cost[1], min_cost[2])
            min_cost1 = cost[1] + min(min_cost[0], min_cost[2])
            min_cost2 = cost[2] + min(min_cost[0], min_cost[1])
            min_cost[0] = min_cost0
            min_cost[1] = min_cost1
            min_cost[2] = min_cost2
        return min(min_cost)
