"""
https://leetcode.cn/problems/random-pick-with-blacklist/

给定一个整数 n 和一个 无重复 黑名单整数数组 blacklist 。

设计一种算法，从 [0, n - 1] 范围内的任意整数中选取一个 未加入 黑名单 blacklist 的整数。

任何在上述范围内且不在黑名单 blacklist 中的整数都应该有 同等的可能性 被返回。

优化你的算法，使它最小化调用语言 内置 随机函数的次数。

实现 Solution 类:

- Solution(int n, int[] blacklist) 初始化整数 n 和被加入黑名单 blacklist 的整数
- int pick() 返回一个范围为 [0, n - 1] 且不在黑名单 blacklist 中的随机整数

"""
import random
from typing import List


class Solution:
    """
    哈希映射
    官方题解：https://leetcode.cn/problems/random-pick-with-blacklist/solution/hei-ming-dan-zhong-de-sui-ji-shu-by-leet-cyrx/

    官方题解不是很好懂，可以参考其他人的解析：
    https://leetcode.cn/problems/random-pick-with-blacklist/solution/by-meteordream-xggn/

    参考官解的做法，实际上可取的值为 n - mn−m 个，将黑名单的 mm 个数值映射为 n - mn−m ~ nn 中的数字即可。
    通俗的说，我们将 [0, n - m)[0,n−m) 中在黑名单的数字拿掉，然后用 [n - m, n)[n−m,n) 中不在黑名单中的数字填上，
    但我们不能列出完整的 [0, n - m)[0,n−m) 数组，所以只用哈希表记录那些替换掉的即可。
    """
    def __init__(self, n: int, blacklist: List[int]):
        m = len(blacklist)
        self.bound = w = n - m
        black = {b for b in blacklist if b >= self.bound}
        self.b2w = {}
        for b in blacklist:
            if b < self.bound:
                while w in black:
                    w += 1
                self.b2w[b] = w
                w += 1

    def pick(self) -> int:
        x = random.randrange(self.bound)
        return self.b2w.get(x, x)


class Solution3:
    """
    1. 根据blacklist把原数列有序分段，并记录每一段的大小，
    2. 记total=分段和，也是去除掉blacklist之后剩余的样本空间大小
    3. 取x=rand(1, total+1), 根据随机数x查找落入的分段位(使用二分查找)，在该分段随机一个元素出来

    执行用时：384 ms, 在所有 Python3 提交中击败了24.72%的用户
    内存消耗：24.6 MB, 在所有 Python3 提交中击败了85.16%的用户
    """
    def __init__(self, n: int, blacklist: List[int]):
        self.ranges = []
        blacklist.sort()
        total, start, end = 0, 0, n
        for i in blacklist:
            if i > start:
                total += i - start
                self.ranges.append((total, start, i))
            start = i + 1
        if end > start:
            total += end - start
            self.ranges.append((total, start, end))

        self.total = total

    def pick(self) -> int:
        x = random.randrange(1, self.total + 1)
        left, right = 0, len(self.ranges) - 1
        while right > left:
            mid = (left + right) >> 1
            if x > self.ranges[mid][0]:
                left = mid + 1
            else:
                right = mid

        return random.randrange(*self.ranges[left][1:])


class Solution2:
    """
    1. 根据blacklist把原数列有序分段，并记录每一段的大小，
    2. 记total=分段和，也是去除掉blacklist之后剩余的样本空间大小
    3. 取x=rand(1, total+1), 根据随机数x查找落入的分段位，在该分段随机一个元素出来

    执行用时：6684 ms, 在所有 Python3 提交中击败了5.11%的用户
    内存消耗：24.9 MB, 在所有 Python3 提交中击败了75.91%的用户
    """
    def __init__(self, n: int, blacklist: List[int]):
        self.ranges = []
        blacklist.sort()
        total, start, end = 0, 0, n
        for i in blacklist:
            if i > start:
                total += i - start
                self.ranges.append((total, start, i))
            start = i + 1
        if end > start:
            total += end - start
            self.ranges.append((total, start, end))

        self.total = total

    def pick(self) -> int:
        x = random.randrange(1, self.total + 1)
        # TODO: 二分
        for total, start, end in self.ranges:
            if x <= total:
                return random.randrange(start, end)


class Solution1:
    """
    超时
    66 / 68 个通过测试用例
    """
    def __init__(self, n: int, blacklist: List[int]):
        blackset = set(blacklist)
        self.nums = []
        for i in range(n):
            if i not in blackset:
                self.nums.append(i)
        self.size = len(self.nums)

    def pick(self) -> int:
        if not self.nums:
            return None
        return self.nums[random.randrange(self.size)]


if __name__ == "__main__":
    s = Solution(4, [])
    print(s.total, s.ranges)
    for _ in range(7):
        print(s.pick())