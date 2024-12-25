# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Iterative Method
        # Time O(n)
        # Space O(n)
        dummy = ListNode(0)  # Dummy node to simplify list creation
        current = dummy  # Pointer to construct the result list
        carry = 0
        
        while l1 or l2 or carry:
            # Get values from l1 and l2, or 0 if they are None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)  # Add new node with the sum digit
            
            # Move pointers forward
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Return the result list, skipping the dummy node
        return dummy.next

        # sumList = ret = ListNode(0, None)
        # sum, carry = 0, 0

        # while l1 or l2:
        #     sum = 0
        #     if l1:
        #         sum += l1.val
        #         l1 = l1.next
        #     else:
        #         sum = 0
            
        #     if l2:
        #         sum += l2.val
        #         l2 = l2.next
        #     else:
        #         sum += 0
            
        #     sum += carry
        #     carry = sum // 10
        #     sum = sum % 10
        #     if carry < 0:
        #         carry = 0
            
        #     sumList.val = sum
        #     if l1 or l2:
        #         sumList.next = ListNode(0, None)
        #         sumList = sumList.next
        
        # if carry > 0:
        #     sumList.next = ListNode(carry, None)
        
        # return ret
