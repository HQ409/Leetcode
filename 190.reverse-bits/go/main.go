package main

import "fmt"

/*
输入: 00000010100101000001111010011100
输出: 00111001011110000010100101000000
解释: 输入的二进制串 00000010100101000001111010011100 表示无符号整数 43261596，
     因此返回 964176192，其二进制表示形式为 00111001011110000010100101000000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

func reverseBits(num uint32) uint32 {
    var ret, i uint32 = 0, 1
	// 遍历num的高位1，不用遍历32次
	for num > 0 {
		ret |= (num & 0x80000000) >> (32 - i)
		num <<= 1
		i++
	}
	return ret
}

func main() {
	var num uint32 = 43261596
	rnum := reverseBits(num)
	fmt.Printf(" input = %032b\noutput = %032b\n", num, rnum)
}
