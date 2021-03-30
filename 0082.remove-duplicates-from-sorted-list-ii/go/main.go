package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	// 递归方法
	if head == nil || head.Next == nil {
		return head
	}
	p := deleteDuplicates(head.Next)
	// 记deleteDuplicates为[]符号
	if head.Val == head.Next.Val {
		// head = 1 + [1,1,2,2]
		if p == nil {
			head = nil
			// head = 1 + [1,2]
		} else if head.Val == p.Val {
			head = p.Next
			// head = 1 + [1,1,2]
		} else {
			head = p
		}
	} else {
		// head.Val < head.Next.Val <= p.Val
		// head = 1 + [2,2,3,3,4]
		head.Next = p
	}
	return head
}

func construct(nums []int) *ListNode {
	h := ListNode{}
	p := &h
	for _, n := range nums {
		p.Next = &ListNode{Val: n}
		p = p.Next
	}
	return h.Next
}

func print(node *ListNode) {
	for node != nil {
		fmt.Printf("%v ", node.Val)
		node = node.Next
	}
	fmt.Println()
}

func main() {
	nums := []int{1, 2, 3, 3, 4, 4, 5}
	listnode := construct(nums)
	listnode = deleteDuplicates(listnode)
	print(listnode)
}
