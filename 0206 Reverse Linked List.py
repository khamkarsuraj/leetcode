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
        # Reversing links between nodes results code
        prev, current = None, head

        while current is not None:
            hold = current.next
            current.next = prev
            prev = current
            current = hold

        # return prev pointer which is last element of list
        return prev
