package Java;

/**
 * @see <a href="https://leetcode-cn.com/problems/rotate-list/submissions/"></a>
 * 61. 旋转链表
 */
class Solution61 {
    public ListNode rotateRight(ListNode head, int k) {
        //先循环，获取链表大小
        if (head == null || head.next == null) {
            return head;
        }
        if (k == 0) {
            return head;
        }
        int length = 1;
        ListNode currentNode = head;
        while (currentNode.next != null) {
            length++;
            currentNode = currentNode.next;
        }

        int realRotateNum = length - k % length;
        if (realRotateNum == 0 || realRotateNum == length) {
            return head;
        }
        currentNode = head;

        ListNode oldHeadMarkNode = head;
        while (currentNode.next != null && realRotateNum > 1) {
            currentNode = currentNode.next;
            realRotateNum--;
        }

        ListNode realHeadMarkNode = currentNode.next;
        currentNode.next = null;
        currentNode = realHeadMarkNode;
        while (currentNode.next != null) {
            currentNode = currentNode.next;
        }
        currentNode.next = oldHeadMarkNode;

        return realHeadMarkNode;

    }

    public static void main(String[] s) throws Exception {
        Solution61 q82 = new Solution61();
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

        ListNode listNode1 = new ListNode("listNode1", 1);
        ListNode listNode2 = new ListNode("listNode2", 2);
        // ListNode listNode3 = new ListNode("listNode3", 3);
        // ListNode listNode4 = new ListNode("listNode4", 4);
        // ListNode listNode5 = new ListNode("listNode5", 5);
        listNode1.next = listNode2;
        // listNode2.next = listNode3;
        // listNode3.next = listNode4;
        // listNode4.next = listNode5;
        ListNode result = q82.rotateRight(listNode1, 2);
        System.out.println(result);

    }
}
