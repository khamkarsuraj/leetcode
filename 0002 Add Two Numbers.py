# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sumList = ret = ListNode(0, None)
        sum, carry = 0, 0

        while l1 or l2:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            else:
                sum = 0
            
            if l2:
                sum += l2.val
                l2 = l2.next
            else:
                sum += 0
            
            sum += carry
            carry = sum // 10
            sum = sum % 10
            if carry < 0:
                carry = 0
            
            sumList.val = sum
            if l1 or l2:
                sumList.next = ListNode(0, None)
                sumList = sumList.next
        
        if carry > 0:
            sumList.next = ListNode(carry, None)
        
        return ret
