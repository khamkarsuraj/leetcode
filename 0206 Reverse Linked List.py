# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Iterative Approach
    # Time: O(n)
    # Space: O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if list is empty or single element, return empty list as it is
        if head is None or head.next is None:
            return head
        
        # here we are swaping the links between nodes
        # swaping links between nodes results code to execute in O(n) of time and O(1) space 
        prev = head
        current = head.next

        while current is not None:
            hold = current.next
            current.next = prev
            prev = current
            current = hold
        
        # mark next of first node to NULL to avoid cycle in list
        head.next = None

        # return prev pointer which is last element of list
        return prev
