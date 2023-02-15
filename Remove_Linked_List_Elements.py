# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Approach 1: Iterate through whole list and delete node if found
        # Time Complexity: O(n) | Space Complexity: O(1)
        if not head:
            return head

        prev = curr = head
        # iterate till end node
        while curr:
            # assign next of current to previous node
            # this will delete current node
            if curr.val == val:
                prev.next = curr.next
                curr = prev.next
            # go to next node if it's not target node
            else:
                prev = curr
                curr = curr.next

        if head.val == val:
            return head.next
        return head
