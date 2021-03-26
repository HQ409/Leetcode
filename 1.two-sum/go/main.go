package main

import "fmt"

func twoSum(nums []int, target int) []int {
	m := make(map[int]int, len(nums))
	for index, value := range nums {
		if v, ok := m[target-value]; ok {
			return []int{v, index}
		}
		m[value] = index
	}
	return nil
}

func main() {
	nums := []int{2,7,11,15}
	target := 9
	fmt.Println(twoSum(nums, target))
}
