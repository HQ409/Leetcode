"""
https://leetcode.cn/problems/encode-and-decode-tinyurl

TinyURL 是一种 URL 简化服务， 
比如：当你输入一个 URL https://leetcode.com/problems/design-tinyurl 时，它将返回一个简化的URL http://tinyurl.com/4e9iAk 。
请你设计一个类来加密与解密 TinyURL 。

加密和解密算法如何设计和运作是没有限制的，你只需要保证一个 URL 可以被加密成一个 TinyURL ，并且这个 TinyURL 可以用解密方法恢复成原本的 URL 。

实现 Solution 类：

- Solution() 初始化 TinyURL 系统对象。
- String encode(String longUrl) 返回 longUrl 对应的 TinyURL 。
- String decode(String shortUrl) 返回 shortUrl 原本的 URL 。题目数据保证给定的 shortUrl 是由同一个系统对象加密的。

"""
import string


class Codec:
    """
    以前工作的时候实现过，自增id + base62算法。

    62个字符的排序可以是乱序的，一定程度上可以预防枚举。

    另外一个常见的需求是，相同long_url生成相同的tiny_url，可以在生成之前查表。

    还有一个问题是过期的短地址如何回收，我的思路是：
    1. base62短地址空间很大，一般的业务根本用不完，不需要回收地址；
    2. 过期的短地址必然在db里有标识，如果用完了6位的短地址，我们可以去db里找出来过期的地址优先分配
    ps. 如果地址都用完了，那就需要增加短地址长度了（增加1位理论上地址空间增加62倍）
    """
    CHARS = string.digits + string.ascii_letters

    def __init__(self):
        self.urls = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        uid = len(self.urls)
        tinyurl = self.base62encode(uid)
        self.urls[tinyurl] = longUrl
        return "http://tinyurl.com/" + tinyurl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        tinyurl = shortUrl.lstrip("http://tinyurl.com/")
        return self.urls.get(tinyurl)

    def base62encode(self, uid: int):
        s = ""
        while 1:
            s = self.CHARS[uid % 62] + s
            uid //= 62
            if uid <= 0:
                break
        return s


if __name__ == "__main__":
    codec = Codec()
    origin_url = "https://leetcode.com/problems/design-tinyurl"
    short_url = codec.encode(origin_url)
    long_url = codec.decode(short_url)
    print(origin_url, short_url, long_url)

