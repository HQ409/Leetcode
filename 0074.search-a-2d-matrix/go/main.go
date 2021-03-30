package main

import (
	"fmt"
)

/*
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/

func searchMatrix(matrix [][]int, target int) bool {
	return searchMatrix2(matrix, target)
}

func searchMatrix1(matrix [][]int, target int) bool {
	/*
		先找行再找列
	*/
	rows, cols := len(matrix), len(matrix[0])
	if rows == 0 || cols == 0 || matrix[0][0] > target || matrix[rows-1][cols-1] < target {
		return false
	}
	// 找行
	i, j, row := 0, rows-1, 0
	for i <= j {
		row = (i + j) / 2
		if matrix[row][0] > target {
			j = row - 1
		} else if matrix[row][cols-1] < target {
			i = row + 1
		} else {
			break
		}
	}
	// 找列
	i, j = 0, cols-1
	for i <= j {
		mid := (i + j) / 2
		if matrix[row][mid] > target {
			j = mid - 1
		} else if matrix[row][mid] < target {
			i = mid + 1
		} else {
			return true
		}
	}
	return false
}

func searchMatrix2(matrix [][]int, target int) bool {
	/*
		由于矩阵整个是有序的，所以可以当作一个有序数组，只用一次二分查找
	*/
	m := len(matrix)

	if m == 0 {
		return false
	}
	n := len(matrix[0])

	l := 0
	r := m*n - 1

	for l <= r {
		mid := (l + r) / 2
		if matrix[mid/n][mid%n] == target {
			return true
		} else if matrix[mid/n][mid%n] > target {
			r = mid - 1
		} else {
			l = mid + 1
		}
	}
	return false
}

func main() {
	matrix := [][]int{
		{1, 3, 5, 7},
		{10, 11, 16, 20},
		{23, 30, 34, 60},
	}
	ret := searchMatrix(matrix, 60)
	fmt.Println(ret)
}
