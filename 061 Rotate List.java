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
    public ListNode rotateRight(ListNode head, int k) {
        //Two Pointers
        //Time: O(n)
        //Space: O(1)
        if (head == null) return head;

        ListNode prev = head, current = head;
        int len = 0;

        while (current.next != null) {
            len = len + 1;
            current = current.next;
        }

        len = len+1;
        k = k%len; //IMP

        if (k == 0) {
            return head;
        }

        k = len - k; //IMP
        current.next = head;
        current = head;

        while(k != 0) {
            prev = current;
            current = current.next;
            k = k - 1;
        }

        head = current;
        prev.next = null;
        return head;

        // //Two pointers
        // //Time: O(2n)
        // //Space: O(1)
        // if (head == null) return head;

        // ListNode t1 = head, t2 = head;
        // boolean flag = false;
        // int count = 0;

        // //Find length of LL
        // while (t2 != null) {
        //     count = count + 1;
        //     t2 = t2.next;
        // }
        
        // //Major thing, check how many times actually you need to roatate
        // n = n%count;
        // t2 = head;

        // //Start finding what would be that head and tail 
        // while (t2.next != null) {

        //     if (!flag) t2 = t2.next;
        //     else flag = false;
    
        //     //start moving tail pointer
        //     if (n < 1) {
        //         t1 = t1.next;
        //     }

        //     n = n - 1;

        //     //If you already reached to last node, but still need to rotate
        //     if (t2.next == null && n > 0) {
        //         t2 = head;
        //         flag = true;
        //     }
        // }
        
        // //Break and make Links
        // t2.next = head;
        // head = t1.next;
        // t1.next = null;

        // return head;

    }
}
