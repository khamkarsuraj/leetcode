# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      # create current node and result list for return
        res_list = current = ListNode(0)
        
        # traverse till one of the list gets empty
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # append the remaining nodes from longer list if length of two lists are not same
        current.next = list1 or list2
        
        # return result list except first node, as we have created first node with 0.
        return res_list.next
