# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Approach 0: Using two pointers
    # Time Complexity: O(n) | Space Complexity: O(1)

    def isPalindrome(self, head) -> bool:
        # If only one node is there, return True
        if not head.next:
            return True
        
        # Find middle node
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse the remaining list starting from next of middle node
        # we can write seperate function for reverse logic
        # rev = self.reverse(slow.next) 
        prev = slow.next
        current = slow.next.next

        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        slow.next.next = None

        # Compare reversed and original list till middle node
        slow = head
        while prev:
            if slow.val != prev.val:
                return False
            slow = slow.next
            prev = prev.next

        return True

    # Approach 1: Create list of values from linked list and
    #             cross check it
    # Time Complexity: O(n) | Space Complexity: O(n)
    '''
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        st = []

        root = head
        i=0
        while root:
            st.append(root.val)
            i+=1
            root = root.next

        i = 0
        while i<len(st)//2:
            if st[i] != st[len(st)-1-i]:
                return False
            i+=1

        return True
    '''
