/*
	双指针解法，思路过程参考以下题解
	https://leetcode-cn.com/problems/volume-of-histogram-lcci/solution/li-kou-jia-jia-shuang-zhi-zhen-mian-shi-tw9al/
	https://leetcode-cn.com/problems/volume-of-histogram-lcci/solution/cchao-100de-shuang-zhi-zhen-by-ffreturn-u4fw/
*/
package main

import "fmt"

func trap(height []int) (ans int) {
	if len(height) < 3 {
		return
	}
	left, right := 0, len(height)-1
	leftMax, rightMax := 0, 0
	for left < right {
		leftMax = max(leftMax, height[left])
		rightMax = max(rightMax, height[right])
		if height[left] < height[right] {
			ans += leftMax - height[left]
			left++
		} else {
			ans += rightMax - height[right]
			right--
		}
	}
	return
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	inputs := [][]int{
		{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1},
	}
	for _, input := range inputs {
		ret := trap(input)
		fmt.Printf(" input = %v\noutput = %v\n\n", input, ret)
	}
}
