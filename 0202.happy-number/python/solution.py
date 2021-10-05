# -*- coding: utf-8 -*-


class Solution:
    def isHappy(self, n: int) -> bool:
        while 1:
            n = self.trans(n)
            if n == 1:
                return True
            # 蒙的。数学原理详见：https://leetcode-cn.com/problems/happy-number/solution/kuai-le-shu-by-leetcode-solution/
            # 首先关于数列收敛的证明，然后找规律，发现不收敛为1的序列只有一条路径
            if n == 4:
                return False
        return False

    def trans(self, n: int) -> int:
        ret = 0
        while n > 0:
            ret += (n % 10) ** 2
            n //= 10
        return ret


if __name__ == "__main__":
    n = 31
    s = Solution()
    print(n, s.isHappy(n))