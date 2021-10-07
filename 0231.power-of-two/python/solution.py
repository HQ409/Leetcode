# -*- coding: utf-8 -*-


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 二分，极慢
        if n < 0 or (n > 1 and n % 2 == 1):
            return False
        p, q = 0, n // 2
        while p < q:
            mid = (p + q) // 2
            t = 2**mid
            if t < n:
                p = mid + 1
            else:
                q = mid
        return 2**p == n

    def isPowerOfTwo2(self, n: int) -> bool:
        # 直接除
        if n <= 0:
            return False

        while n % 2 == 0:
            n //= 2
        return n == 1

    def isPowerOfTwo3(self, n: int) -> bool:
        # 加速除
        if n <= 0:
            return False

        p = 1
        while 1:
            if p < 1:
                return False
            mod = 2**p
            if n % mod == 0:
                n //= mod
                if n == 1:
                    return True
                p <<= 1
            else:
                p >>= 1
        return True

    def isPowerOfTwo4(self, n: int) -> bool:
        # 利用位运算判断二进制是否只有一个1
        return (n > 0) and (n & (n - 1) == 0)


if __name__ == "__main__":
    s = Solution()
    # print(1073741825, s.isPowerOfTwo(1073741825))
    # print(2, s.isPowerOfTwo(2))
    # print(3, s.isPowerOfTwo(3))
    # print(5, s.isPowerOfTwo(5))
    # print(1, s.isPowerOfTwo(1))
    # print(16, s.isPowerOfTwo3(16))
    print(1024, s.isPowerOfTwo2(65536))     # 循环16次
    print(1024, s.isPowerOfTwo3(65536))     # 循环9次