# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Two Pointers
        # Time: O(n)
        # Space: O(1)
        if (head == None):
            return head

        prev = current = head
        len = 0

        while (current.next != None):
            len += 1
            current = current.next

        len += 1
        k = k % len 

        if (k == 0):
            return head

        k = len - k - 1
        current.next = head

        while(k != 0):
            prev = prev.next
            k -= 1

        head = prev.next
        prev.next = None
        return head

        # if (head == None):
        #     return head

        # t1 = t2 = head
        # flag = False
        # count = 0

        # while (t2 != None):
        #     count += 1
        #     t2 = t2.next
        
        # n=n%count
        # t2 = head

        # while t2.next != None:
        #     if not flag:
        #         t2 = t2.next
        #     else:
        #         flag = False
    
        #     if n < 1:
        #         t1 = t1.next

        #     n -= 1

        #     if (t2.next == None and n > 0):
        #         t2 = head
        #         flag = True
        
        # t2.next = head
        # head = t1.next
        # t1.next = None

        # return head
