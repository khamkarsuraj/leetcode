/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        //Two Pointer
        //Time: O(n)
        //Space: O(1)
        //Corner Cases
        if (head == null) return head;
        if (head.next == null) return head;

        //p - previous pointer to the pointers to be swap
        //p1, p2 - actual pointers to be swap
        //n - next pointer to the pointers to be swap
        ListNode p, p1, p2, n;
        //Assign pointers for initial operation
        p = head;
        p1 = head;
        p2 = head.next;
        n = p2.next;

        while (p2 != null) {
            p2.next = p1;
            //If this is first swapping
            if (p == head) {
                p.next = p2;
                head = p2;
            } else {
                p.next = p2;
            }
            p1.next = n;

            p = p1;
            p1 = n;
            //If we swapped last two nodes already Or length of the LL is odd
            //then don't go forward, exit from loop by assigning p2 = null
            if (n != null && n.next != null) {
                p2 = n.next;
                n = n.next.next;
            } else {
                p2 = null;
            }
        }

        return head;
    }
}
