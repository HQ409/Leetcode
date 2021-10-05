# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 递归方法
        if head is None or head.next is None:
            return head
        h = self.reverseList(head.next)
        cur = h
        while cur.next:
            cur = cur.next
        cur.next = head
        # 15至18行的目的是为了找到已翻转的链表的最后一个节点，并和当前节点连接起来
        # 考虑到reverseList(head.next)之后，head.next肯定是最后一个节点，所以可以用一行代码替代：head.next.next = head
        head.next = None
        return h

    def reverseList2(self, head: ListNode) -> ListNode:
        # 迭代方法：https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/
        prev = None
        cur = head
        while cur:
            t = cur.next
            cur.next = prev
            prev = cur
            cur = t
        return prev

    def printList(self, head: ListNode):
        while head:
            print(head.val)
            head = head.next

    def makeList(self, nums) -> ListNode:
        head = ListNode()
        cur = head
        for n in nums:
            cur.next = ListNode(n)
            cur = cur.next
        return head.next


if __name__ == "__main__":
    s = Solution()
    head = s.makeList([1, 2, 3, 4, 5])
    s.printList(s.reverseList2(head))