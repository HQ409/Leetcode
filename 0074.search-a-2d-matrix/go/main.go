package main

import "fmt"

func searchMatrix(matrix [][]int, target int) bool {
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

func main() {
	matrix := [][]int{
		{1, 3, 5, 7},
		{10, 11, 16, 20},
		{23, 30, 34, 60},
	}
	ret := searchMatrix(matrix, 60)
	fmt.Println(ret)
}
