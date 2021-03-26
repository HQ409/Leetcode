package main

import "fmt"

func spiralOrder(matrix [][]int) []int {
	m := len(matrix)    // 行数
	n := len(matrix[0]) // 列数
	total := m * n
	output := make([]int, total)
	visited := create2dSlice(m, n)
	p, q, gone := 0, 0, 0
	output[gone] = matrix[p][q]
	visited[p][q] = 1
	for gone < total - 1 {
		// 向右
		for q < n-1 && visited[p][q+1] == 0 {
			gone++; q++
			output[gone] = matrix[p][q]
			visited[p][q] = 1
		}
		// 向下
		for p < m-1 && visited[p+1][q] == 0 {
			gone++; p++
			output[gone] = matrix[p][q]
			visited[p][q] = 1
		}
		// 向左
		for q > 0 && visited[p][q-1] == 0 {
			gone++; q--
			output[gone] = matrix[p][q]
			visited[p][q] = 1
		}
		// 向上
		for p > 0 && visited[p-1][q] == 0 {
			gone++; p--
			output[gone] = matrix[p][q]
			visited[p][q] = 1
		}
	}
	return output
}

func spiralOrderWrong1(matrix [][]int) []int {
	/*
		这个解法基本思路是对的，但是细节处理有问题。
		方向应该是固定的，直到走不通的时候才重新检测，而不是每走一步都检测一次方向
	*/
	m := len(matrix)    // 行数
	n := len(matrix[0]) // 列数
	total := m * n
	output := make([]int, total)
	visited := create2dSlice(m, n)
	p, q, gone := 0, 0, 0
	for gone < total {
		output[gone] = matrix[p][q]
		visited[p][q] = 1
		if q < n-1 && visited[p][q+1] == 0 {
			// 先向右走
			q++
		} else if p < m-1 && visited[p+1][q] == 0 {
			// 再向下走
			p++
		} else if q > 0 && visited[p][q-1] == 0 {
			// 再向左走
			q--
		} else {
			// 最后向上走
			p--
		}
		gone++
	}
	return output
}

func create2dSlice(row, col int) [][]int {
	s := make([][]int, row)
	for k := range s {
		s[k] = make([]int, col)
	}
	return s
}

func main() {
	input := [][]int{
		{1, 2, 3, 4},
		{5, 6, 7, 8},
		{9, 10, 11, 12},
	}
	output := spiralOrder(input)
	fmt.Println(output)

	input2 := [][]int{
		{1, 2, 3, 4},
		{5, 6, 7, 8},
		{9, 10, 11, 12},
		{13, 14, 15, 16},
	}
	output2 := spiralOrder(input2)
	fmt.Println(output2)
}
