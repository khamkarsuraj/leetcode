"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Using List Interweave
        # Time O(n)
        # Space O(n)
        # if not head:
        #     return head

        # # First interweave old and new list
        # curr = head
        # while curr:
        #     copy = Node(curr.val, curr.next)
        #     curr.next = copy
        #     curr = copy.next

        # # Then, copy random pointers to new list
        # curr = head
        # while curr:
        #     if curr.random:
        #         curr.next.random = curr.random.next
        #     curr = curr.next.next

        # # Now, separate old and new list
        # copy_head = head.next
        # copy_curr = copy_head
        # curr = head
        # while curr:
        #     curr.next = curr.next.next
        #     if copy_curr.next:
        #         copy_curr.next = copy_curr.next.next
        #     curr = curr.next
        #     copy_curr = copy_curr.next

        # return copy_head

        # Using HashMap
        # Time O(n)
        # Space O(n)
        if not head:
            return None

        nodeMap = {None: None}
        cur = head

        while cur:
            newNode = Node(cur.val)
            nodeMap[cur] = newNode
            cur = cur.next

        cur = head
        while cur:
            #copy.next, copy.random
            nodeMap[cur].next = nodeMap[cur.next]
            nodeMap[cur].random = nodeMap[cur.random]
            cur = cur.next

        return nodeMap[head]

        # Using copy lib
        # return copy.deepcopy(head)
