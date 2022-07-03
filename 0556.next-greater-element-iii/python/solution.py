"""
https://leetcode.cn/problems/next-greater-element-iii/

给你一个正整数 n ，请你找出符合条件的最小整数，其由重新排列 n 中存在的每位数字组成，并且其值大于 n 。如果不存在这样的正整数，则返回 -1 。

注意 ，返回的整数应当是一个 32 位整数 ，如果存在满足题意的答案，但不是 32 位整数 ，同样返回 -1 。

"""


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n < 10:
            return -1

        # 取最低位数字
        digits = [n % 10]
        n //= 10

        # 从次低位数字开始往高位比较
        # digits是依序保存不高于前一位的数字，容易证明它是一个（非严格）递增数组
        while n > 0:
            digit = n % 10
            # 低位最大数字大于高位数字，准备交换
            if digits[-1] > digit:
                break
            digits.append(digit)
            n //= 10

        if n == 0:
            return -1

        # 从小到大遍历digits数组，交换digits大于高位数字的最小位
        for i in range(len(digits)):
            if digits[i] > digit:
                min_digit = digits[i]
                digits[i] = digit
                break

        # 组合高低位数字
        ret = n - digit + min_digit
        for i in range(len(digits)):
            ret = ret * 10 + digits[i]

        return ret if ret < 2**31 else -1


if __name__ == "__main__":
    s = Solution()
    print(564321, s.nextGreaterElement(564321))
    # print(1200, s.nextGreaterElement(1200))
    # print(2147483476, s.nextGreaterElement(2147483476))
