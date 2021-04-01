package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

func subsetsWithDup(nums []int) (ans [][]int) {
	// 官方解法
	sort.Ints(nums)
	n := len(nums)
outer:
	for mask := 0; mask < 1<<n; mask++ {
		t := []int{}
		for i, v := range nums {
			if mask>>i&1 > 0 {
				if i > 0 && mask>>(i-1)&1 == 0 && v == nums[i-1] {
					continue outer
				}
				t = append(t, v)
			}
		}
		ans = append(ans, append([]int(nil), t...))
	}
	return
}

func subsetsWithDupMine(nums []int) [][]int {
	// 我的解法
	// 思路类似：https://leetcode-cn.com/problems/subsets-ii/solution/python-yi-ci-bian-li-mo-ni-bu-xu-yao-hui-3149/
	subsets := [][]int{{}}
	sort.Ints(nums)
	for j := 0; j < len(nums); j++ {
		vals := []int{}
		newSubsets := [][]int{}
		for {
			vals = append(vals, nums[j])
			for _, subset := range subsets {
				s := make([]int, 0, len(subsets)+len(vals))
				s = append(s, subset...)
				s = append(s, vals...)
				newSubsets = append(newSubsets, s)
			}
			if j >= len(nums)-1 || nums[j] != nums[j+1] {
				break
			}
			j++
		}
		subsets = append(subsets, newSubsets...)
	}
	return subsets
}

func subsetsWithDupStupid(nums []int) [][]int {
	subsets := make(map[string]bool)
	subsets[""] = true
	sort.Ints(nums)
	for _, n := range nums {
		s := strconv.Itoa(n)
		newKeys := []string{}
		for subset := range subsets {
			key := s
			if len(subset) != 0 {
				key = strings.Join([]string{subset, key}, ".")
			}
			if _, ok := subsets[key]; !ok {
				newKeys = append(newKeys, key)
			}
		}
		for _, key := range newKeys {
			subsets[key] = true
		}
	}
	ret := [][]int{}
	for subset := range subsets {
		numList := []int{}
		if len(subset) > 0 {
			for _, char := range strings.Split(subset, ".") {
				n, _ := strconv.Atoi(char)
				numList = append(numList, n)
			}
		}
		ret = append(ret, numList)
	}
	return ret
}

func main() {
	inputs := [][]int{
		{1, 2, 2},
		{9, 0, 3, 5, 7},
		{5, 5, 5, 5, 5},
		{0},
		{-1, 1, 2},
	}
	for _, input := range inputs {
		ret := subsetsWithDup(input)
		fmt.Printf(" input = %v\noutput = %v\n\n", input, ret)
	}
}
