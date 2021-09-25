/*
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 最多出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

package main

import "fmt"

func removeDuplicates(nums []int) int {
	if len(nums) < 3 {
		return len(nums)
	}
	cur := 0
	cnt := 1
	for i := cur + 1; i < len(nums); i++ {
		if nums[i] == nums[cur] {
			cnt += 1
			if cnt <= 2 {
				cur += 1
				nums[cur] = nums[i]
			}
		} else {
			cnt = 1
			cur += 1
			nums[cur] = nums[i]
		}
	}
	return cur + 1
}

func main() {
	inputs := [][]int{
		{1, 1, 1, 2, 2, 3},
		{0, 0, 1, 1, 1, 1, 2, 3, 3},
	}
	for _, input := range inputs {
		origin := make([]int, len(input))
		copy(origin, input)
		ret := removeDuplicates(input)
		fmt.Printf(" input = %v\noutput = %v\n\n", origin, input[:ret])
	}
}
