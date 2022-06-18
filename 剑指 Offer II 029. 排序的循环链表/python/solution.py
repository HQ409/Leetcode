"""
https://leetcode.cn/problems/4ueAj6/

给定循环单调非递减列表中的一个点，写一个函数向这个列表中插入一个新元素 insertVal ，使这个列表仍然是循环升序的。

给定的可以是这个列表中任意一个顶点的指针，并不一定是这个列表中最小元素的指针。

如果有多个满足条件的插入位置，可以选择任意一个位置插入新的值，插入后整个列表仍然保持有序。

如果列表为空（给定的节点是 null），需要创建一个循环有序列表并返回这个节点。否则。请返回原先给定的节点。

"""
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        insertNode = Node(insertVal)

        # 空链表，直接返回insertNode
        if not head:
            head = insertNode
            insertNode.next = head
            return head

        # 单节点链表，把head，insertNode首尾相连后返回
        if head.next == head:
            head.next = insertNode
            insertNode.next = head
            return head

        cur = head
        min_node = None
        max_node = None
        while True:
            if insertVal >= cur.val and insertVal <= cur.next.val:
                insertNode.next = cur.next
                cur.next = insertNode
                cur = insertNode
                break

            if not min_node or min_node.val > cur.val:
                # 第一个最小节点
                min_node = cur

            if not max_node or max_node.val <= cur.val:
                # 最后一个最大节点
                max_node = cur

            cur = cur.next
            if cur == head:
                break

        # 没有在中间插入, 需要在两边插入
        if cur != insertNode:
            # 因为是单调非递减循环链表，所以max_node.next == min_node
            if insertVal < min_node.val:
                # 插入第一个最小节点之前
                insertNode.next = min_node
                max_node.next = insertNode
            elif insertVal > max_node.val:
                # 插入最后一个最大节点之后
                insertNode.next = max_node.next
                max_node.next = insertNode

        return head


class Solution2:
    """
    大致思路同Solution1, 逻辑进行简化：

    只要没有在遍历过程中插入节点，就说明插入值在原链表值域之外
    且在循环列表中，『插入第一个最小节点之前』和『插入最后一个最大节点之后』是等价的，因此无需关心插入的具体值，只需要记录一个最大节点的位置即可。
    """
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        insertNode = Node(insertVal)

        if not head:
            head = insertNode
            insertNode.next = head
            return head

        if head.next == head:
            head.next = insertNode
            insertNode.next = head
            return head

        cur = head
        max_node = None
        while True:
            if not max_node or max_node.val <= cur.val:
                # 最后一个最大节点
                max_node = cur

            if insertVal >= cur.val and insertVal <= cur.next.val:
                insertNode.next = cur.next
                cur.next = insertNode
                cur = insertNode
                break

            cur = cur.next
            if cur == head:
                break

        # 没有在中间插入, 追加在max_node之后
        if cur != insertNode:
            insertNode.next = max_node.next
            max_node.next = insertNode

        return head


def creat_circular_list(nums: List[int]) -> Node:
    if len(nums) == 0:
        return None

    head = Node(nums[0])
    cur = head
    for n in nums[1:]:
        node = Node(n)
        cur.next = node
        cur = cur.next

    cur.next = head
    return head


def circular_list_to_nums(head: Node) -> List[int]:
    nums = []
    cur = head
    while True:
        if not cur:
            break
        nums.append(cur.val)
        cur = cur.next
        if cur == head:
            break
    return nums


if __name__ == "__main__":
    head = creat_circular_list([3, 4, 1])
    solution = Solution()
    solution.insert(head, 2)
    print(circular_list_to_nums(head))