"""
https://leetcode.cn/problems/longest-uncommon-subsequence-ii

给定字符串列表 strs ，返回其中 最长的特殊序列 。如果最长特殊序列不存在，返回 -1 。

特殊序列 定义如下：该序列为某字符串 独有的子序列（即不能是其他字符串的子序列）。

 s 的 子序列可以通过删去字符串 s 中的某些字符实现。

例如，"abc" 是 "aebdc" 的子序列，因为您可以删除"aebdc"中的下划线字符来得到 "abc" 。"aebdc"的子序列还包括"aebdc"、 "aeb" 和 "" (空字符串)。

"""
from typing import List


class Solution:
    """
    基本同solution2，只是不排序

    这个题目很绕，我们梳理如下：
    1. 假设strs[i]的一个子序列substr是最长的独有子序列，由于substr不是任何其他元素的子序列，
       那么substr的超集str[i]也不是其他任何元素的子序列，那么str[i]自身就是最长特殊序列

    2. 因此题意退化为求数组中最长的那个元素，该元素不是任何其他元素的子序列

    3. 所以最终的算法就是一个二重循环，遍历检查每个元素是不是其他元素的子序列，没有则返回-1
       底层循环优化检查次数比较麻烦，考虑strs数组长度不大，简单起见每次检查都遍历有非自身元素
       （ps. 这里应该是可以优化的，但是试了几次都有错误，感觉优化后的算法也不高明，反而比较难懂，作罢）
    """
    def findLUSlength(self, strs: List[str]) -> int:
        maxlen = -1
        for i in range(len(strs)):
            # 标记i是否是特殊序列
            uniq = True
            for j in range(len(strs)):
                # 排除相同元素
                if j == i:
                    continue
                # 元素i是元素j的子序列，排除i为特殊序列
                if self.issubstr(strs[i], strs[j]):
                    uniq = False
                    break
            # 元素i不是任何其他元素的子序列，结合数组有序特征，即可直接返回
            if uniq:
                maxlen = max(maxlen, len(strs[i]))
        return maxlen

    def issubstr(self, s1: str, s2: str) -> bool:
        """
        判断s1是否是s2的子序列
        """
        if len(s1) > len(s2):
            return False

        p1, p2 = 0, 0
        while p1 < len(s1) and p2 < len(s2):
            if s1[p1] == s2[p2]:
                p1 += 1
            p2 += 1
        return p1 == len(s1)


class Solution2:
    def findLUSlength(self, strs: List[str]) -> int:
        # 字符串从长到短排序，方便后续提前退出
        strs.sort(key=len, reverse=True)

        for i in range(len(strs)):
            # 标记i是否是特殊序列
            uniq = True
            for j in range(len(strs)):
                # 排除相同元素
                if j == i:
                    continue
                # 如果当前元素j长度小于元素i，则无须继续比较
                if len(strs[i]) > len(strs[j]):
                    break
                # 元素i是元素j的子序列，排除i为特殊序列
                if self.issubstr(strs[i], strs[j]):
                    uniq = False
                    break
            # 元素i不是任何其他元素的子序列，结合数组有序特征，即可直接返回
            if uniq:
                return len(strs[i])
        return -1

    def issubstr(self, s1: str, s2: str) -> bool:
        """
        判断s1是否是s2的子序列
        """
        if len(s1) > len(s2):
            return False

        p1, p2 = 0, 0
        while p1 < len(s1) and p2 < len(s2):
            if s1[p1] == s2[p2]:
                p1 += 1
            p2 += 1
        return p1 == len(s1)


class Solution1:
    """
    直接思路，生成每个字符串的所有子序列，然后作比较，排除重复的，取最大长度。

    执行用时： 604 ms , 在所有 Python3 提交中击败了 5.47% 的用户
    内存消耗： 18.8 MB , 在所有 Python3 提交中击败了 8.46% 的用户
    """
    def findLUSlength(self, strs: List[str]) -> int:
        cnt = {}
        for s in strs:
            for substr in self.substrs(s):
                if substr not in cnt:
                    cnt[substr] = 1
                else:
                    cnt[substr] += 1

        maxlen = -1
        for k, v in cnt.items():
            if v == 1 and len(k) > maxlen:
                maxlen = len(k)
        return maxlen

    def substrs(self, s) -> List[str]:
        """生成所有子序列"""
        _substrs = set()
        slen = len(s)
        for i in range(2**slen):
            _substrs.add(self.mask(s, i))
        return _substrs

    def mask(self, s: str, code: int) -> str:
        """按照掩码生成子序列"""
        substr = ""
        slen = len(s)
        for i in range(slen):
            shift = 1 << (slen - i - 1)
            if code & shift:
                substr += s[i]
        return substr


if __name__ == "__main__":
    s = Solution()
    print(s.issubstr("aabbcc", "aabbcc"))
    # print(s.issubstr("abcd", "a1b2c3"))
    assert s.findLUSlength(["aabbcc", "aabbcc", "cb", "abc"]) == 2
    assert s.findLUSlength(["a", "b", "c", "d", "e", "f", "a", "b", "c", "d", "e", "f"]) == -1
    assert s.findLUSlength(["aaa", "aaa", "aa"]) == -1
    assert s.findLUSlength(["aba", "cdc", "eae"]) == 3
