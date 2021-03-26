package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
    p := head
    for p != nil {
        t := p
        for t != nil && p.Val == t.Val {
            t = t.Next
        }
        p.Next = t
        p = p.Next
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
