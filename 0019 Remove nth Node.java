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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        //Using Two pointers
        //Time: O(n)
        //Space: O(1)
        ListNode t1 = head;
        ListNode t2 = head;

        while (t2 != null) {
            t2 = t2.next;
            if (n < 0) t1 = t1.next;
            n = n - 1;
        }         
        
        if (n > -1) {
            head = head.next;
            return head;
        }
        else t1.next = t1.next.next;

        return head;
    }
}
