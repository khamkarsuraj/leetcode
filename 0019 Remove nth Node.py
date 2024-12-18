# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Using Two Pointer
        # Time O(n)
        # Space O(1)
        # Create a dummy node to simplify edge case handling
        dummy = ListNode(0, head)
        fast, slow = dummy, dummy

        # Move the fast pointer `n` steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Remove the target node
        slow.next = slow.next.next

        return dummy.next

        # Using counter
        # Time O(n)
        # Space O(1)
        # Get counter by using 0-n
        # count = 0 - n
        # curr, ptr = head, head

        # while ptr:
        #     # Go till ptr reaches End
        #     ptr = ptr.next
        #     # If count is still less than 0 increase it
        #     if count < 0:
        #         count+=1
        #     # As count >= 0, start tracking curr (to be removed) pointer
        #     else:
        #         prev = curr
        #         curr = curr.next
        
        # # if there is only one element in LL
        # if curr == head:
        #     head = head.next
        # # else remove the target (curr) pointer
        # else:
        #     prev.next = curr.next
        # return head
        
        #Using Two pointers
        #Time: O(n)
        #Space: O(1)
        # t1 = t2 = head

        # while (t2 != None):
        #     t2 = t2.next
        #     if (n < 0):
        #         t1 = t1.next
        #     n -= 1          
        
        # if n > -1:
        #     head = head.next
        #     return head
        # else:
        #     t1.next = t1.next.next

        # return head
        
