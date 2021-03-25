package Java;

/**
 * @see <a href="https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/"></a>
 * 82. 删除排序链表中的重复元素 II
 * 此题目很简单，但是要注意边界值处理
 */
class Solution82 {
    public ListNode deleteDuplicates(ListNode head) {
        //如果是空队列，或者是只有一个值的队列，直接返回成功
        if (head == null || head.next == null) {
            return head;
        }

        //因为从第一个节点就可能重复，所以这里获取不重复的第一个节点
        ListNode startNode = null;
        {
            //上个节点
            ListNode beforeNode = null;
            //当前节点
            ListNode currentNode = head;
            //下一个节点
            ListNode nextNode;

            while (currentNode != null) {
                nextNode = currentNode.next;
                //如果当前节点和前后的节点都不相同，则为初始节点
                if ((beforeNode == null || beforeNode.val != currentNode.val) && (nextNode == null || nextNode.val != currentNode.val)) {
                    startNode = currentNode;
                    break;
                } else {
                    beforeNode = currentNode;
                    currentNode = currentNode.next;
                }
            }

            //可能存在1，1或者1，1，2这种初始节点为空或者为单节点的情况，所以这里进行判断
            if (startNode == null || startNode.next == null) {
                return startNode;
            }
        }

        //获取到初始节点后，从初始节点遍历链表
        {
            //上个节点
            ListNode beforeNode = null;
            //当前节点
            ListNode currentNode = startNode;
            //下一个节点
            ListNode nextNode;

            while (currentNode != null && currentNode.next != null) {
                nextNode = currentNode.next;
                if (currentNode.val == nextNode.val) {
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
                    beforeNode.next = currentNode.next;
                    currentNode = currentNode.next;
                } else {
                    //非重复，就往后走一个节点
                    beforeNode = currentNode;
                    currentNode = currentNode.next;
                }
            }
            return startNode;
        }
    }

    public static void main(String[] s) throws Exception {
        Solution82 q82 = new Solution82();
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


class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    @Override
    public String toString() {
        return "<" + val + ">";
    }
}
