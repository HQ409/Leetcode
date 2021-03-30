package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func rotateRight(head *ListNode, k int) *ListNode {
	n := 0 // 链表长度
	p := head
	for p != nil {
		p = p.Next
		n++
	}
	if n == 0 {
		return head
	}
	// 计算等效右移位置
	k %= n
	if k == 0 {
		return head
	}
	// 找新的头节点之前那个节点的位置
	beforehead := n - k - 1
	p = head
	for i := 0; i < beforehead; i++ {
		p = p.Next
	}
	headNew := p.Next
	// 原链表断掉新头节点
	p.Next = nil
	// 新头节点的尾部连接原链表
	p = headNew
	for p.Next != nil {
		p = p.Next
	}
	p.Next = head
	return headNew
}