# -*- coding: utf-8 -*-
"""
https://leetcode.cn/problems/find-and-replace-pattern/

回想一下，字母的排列是从字母到字母的双射：每个字母映射到另一个字母，没有两个字母映射到同一个字母。

数据定义：双射=单射+满射
"""

from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ret = []
        for word in words:
            # 如果word和pattern可以互相映射，那么他们就是双射
            if self.match(word, pattern):
                ret.append(word)
        return ret
    
    def match(self, word: str, pattern: str) -> bool:
        """
        判断word到pattern双射
        """
        # 判断长度是否相等，不满足则不可能满足双射中的满射条件    
        wordlen = len(word)
        if wordlen != len(pattern):
            return False

        # 先判断能不能从word映射到pattern，类似abb其实也可以映射到ccc，此时映射表为{"a":"c", "b": "c"}，但是这种case不满足条件
        tmpdict = {}
        for i in range(wordlen):
            s = word[i]
            t = pattern[i]
            if t not in tmpdict:
                tmpdict[t] = s
            elif tmpdict[t] != s:
                return False
        
        # 通过检查映射表的唯一k,v数量是否相等来判断是否单射，单射+满射=双射。
        # 这里就可以过滤出上述的无效case，严格数据证明已经忘了，但是可以AC
        return len(set(tmpdict.keys())) == len(set(tmpdict.values()))


class Solution2:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ret = []
        for word in words:
            # 如果word和pattern可以互相映射，那么他们就是双射
            # https://leetcode.cn/problems/find-and-replace-pattern/solution/cha-zhao-he-ti-huan-mo-shi-by-leetcode-s-fyyg/
            if self.match(word, pattern) and self.match(pattern, word):
                ret.append(word)
        return ret

    def match(self, word: str, pattern: str) -> bool:
        """
        判断word可以映射到pattern，但是不一定是单射
        """
        wordlen = len(word)
        if wordlen != len(pattern):
            return False

        tmpdict = {}
        for i in range(wordlen):
            s = word[i]
            t = pattern[i]
            if t not in tmpdict:
                tmpdict[t] = s
            elif tmpdict[t] != s:
                return False
        
        return True