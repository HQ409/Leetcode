/*
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

示例 1：

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
示例 2：

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]

来源：力扣（LeetCode)
链接：https://leetcode-cn.com/problems/merge-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

package main

import "fmt"

func merge(nums1 []int, m int, nums2 []int, n int) {
	/*
	双指针反向合并方法
	正向合并可能会覆盖到原数组的值，反向合并不需要额外数组存储，进行原地合并。

	i=全局数组下标
	m=nums1数组下标，n=nums2数组下标，不使用额外空间，如果不能改变m、n的值，需要使用其他变量代替
	当nums2数组被合并完时，nums1数组已然有序，直接完成合并
	当nums1数组被合并完时，nums2还有数据未处理完，需要把这部分数据copy到nums1数组头部，然后完成合并
	*/
	i := m + n - 1
	m--
	n--
	for {
		if n < 0 {
			break
		}
		if m < 0 {
			copy(nums1, nums2[:n+1])
			break
		}
		if nums1[m] > nums2[n] {
			nums1[i] = nums1[m]
			m--
		} else {
			nums1[i] = nums2[n]
			n--
		}
		i--
	}
}

func main() {
	nums1, m := []int{1, 2, 4, 0, 0, 0}, 3
	nums2, n := []int{3, 5, 6}, 3
	merge(nums1, m, nums2, n)
	fmt.Println(nums1)
}