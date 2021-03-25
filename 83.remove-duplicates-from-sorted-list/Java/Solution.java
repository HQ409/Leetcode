package Java;

/**
 * @see <a href="https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/"></a>
 * 83. 删除排序链表中的重复元素
 * 未完成
 */
class Solution83 {
    public ListNode deleteDuplicates(ListNode head) {
        //如果是空队列，或者是只有一个值的队列，直接返回成功
        if (head == null || head.next == null) {
            return head;
        }

        //上个节点
        ListNode beforeNode = head;
        //当前节点
        ListNode currentNode = head;

        while (currentNode != null && currentNode.next != null) {
            if (currentNode.val == currentNode.next.val) {
                //如果检测到重复，就记录重复值
                int repeatVal = currentNode.val;
                while (currentNode.next != null) {
                    if (currentNode.next.val == repeatVal) {
                        //向后遍历直到和重复值不同，或者到链表尾部情况
                        currentNode = currentNode.next;
                    } else {
                        break;
                    }
                }
                //这里脱出有两种情况，一是链表到头了，或者是遇到了不同的值，但是这两种情况的处理是一样的
                beforeNode.next = currentNode;
                currentNode = currentNode.next;
            } else {
                //非重复，就往后走一个节点
                beforeNode = currentNode;
                currentNode = currentNode.next;
            }
        }
        return head;

    }

    public static void main(String[] s) throws Exception {
        Solution83 q82 = new Solution83();
        // ListNode listNode1=new ListNode(1);
        // ListNode listNode2=new ListNode(2);
        // ListNode listNode3=new ListNode(3);
        // ListNode listNode4=new ListNode(3);
        // ListNode listNode5=new ListNode(4);
        // ListNode listNode6=new ListNode(4);
        // ListNode listNode7=new ListNode(5);
        // listNode1.next=listNode2;
        // listNode2.next=listNode3;
        // listNode3.next=listNode4;
        // listNode4.next=listNode5;
        // listNode5.next=listNode6;
        // listNode6.next=listNode7;
        // ListNode result = q82.deleteDuplicates(listNode1);
        // System.out.println(result);

        // ListNode listNode1=new ListNode(1);
        // ListNode listNode2=new ListNode(1);
        // ListNode listNode3=new ListNode(1);
        // ListNode listNode4=new ListNode(2);
        // ListNode listNode5=new ListNode(3);
        // listNode1.next=listNode2;
        // listNode2.next=listNode3;
        // listNode3.next=listNode4;
        // listNode4.next=listNode5;
        // ListNode result = q82.deleteDuplicates(listNode1);
        // System.out.println(result);

        ListNode listNode1 = new ListNode(1);
        ListNode listNode2 = new ListNode(1);
        ListNode listNode3 = new ListNode(2);
        listNode1.next = listNode2;
        listNode2.next = listNode3;
        ListNode result = q82.deleteDuplicates(listNode1);
        System.out.println(result);

    }
}

