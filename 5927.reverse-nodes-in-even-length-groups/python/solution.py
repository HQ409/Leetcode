# -*- coding: utf-8 -*-
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        head = self
        nums = []
        while head:
            nums.append(str(head.val))
            head = head.next
        return "->".join(nums)

    @classmethod
    def new(cls, nums):
        head = cls()
        cur = head
        for n in nums:
            cur.next = ListNode(n)
            cur = cur.next
        return head.next


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        gn = 1  # 组序号
        max_n = 1
        n = 1
        p = head
        while p:
            np = p.next
            if not np:
                break
            n += 1
            if n > max_n:
                # 换组
                gn += 1
                max_n += gn
                # 求组实际长度
                gl = 0
                tmp = np
                while tmp:
                    gl += 1
                    if gl >= gn:
                        break
                    tmp = tmp.next
                if gl % 2 == 0:
                    # 反转链表
                    p.next = self.reverseList(np, gl)
                    p = p.next
                else:
                    # 奇数长度
                    p = tmp
                    n += gl - 1
                if gl < gn:
                    # 到结尾了
                    break
            else:
                # 正常遍历
                p = np

        return head

    def reverseList(self, head: ListNode, n: int) -> ListNode:
        """ 反转链表的n个节点 """
        print(f"反转前：{head}, 反转长度：{n}")
        # 获取反转后的尾节点
        prev = head
        i = 0
        while prev and i < n:
            prev = prev.next
            i += 1

        # 反转链表
        cur = head
        while cur and n > 0:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            n -= 1
        print(f"反转后：{prev}")
        return prev

    def makeList(self, nums) -> ListNode:
        head = ListNode()
        cur = head
        for n in nums:
            cur.next = ListNode(n)
            cur = cur.next
        return head.next


def test():
    s = Solution()
    # head = ListNode.new([1, 1, 0, 6])
    # head = s.reverseEvenLengthGroups(head)
    # print(head)
    # head = ListNode.new([0, 4, 2, 1, 3])
    head = ListNode.new([5, 2, 6, 3, 9, 1, 7, 3, 8, 4])
    print(head)
    head = s.reverseEvenLengthGroups(head)
    print(head)


if __name__ == "__main__":
    test()