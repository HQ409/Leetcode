# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        if fast:
            # 奇数个节点
            slow = slow.next

        tail = self.reverseList(slow)
        while head and tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True

    def reverseList(self, head: ListNode) -> ListNode:
        """ 翻转链表 """
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev

    def makeList(self, nums) -> ListNode:
        head = ListNode()
        cur = head
        for n in nums:
            cur.next = ListNode(n)
            cur = cur.next
        return head.next


if __name__ == "__main__":
    s = Solution()
    l1 = s.makeList([1, 2, 3, 4, 5])
    s.isPalindrome(l1)
    l2 = s.makeList([1, 2, 3, 4])
    s.isPalindrome(l2)