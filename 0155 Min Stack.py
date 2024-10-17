# Using two stacks
# One to add 'val'
# Another to keep track of 'min'
class MinStack:
    def __init__(self):
        self.stack = deque()
        self.minStack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

'''
Using Node which keeps track of min value with every 'val' added
class Node:
    def __init__(self, val, min):
        self.val = val
        self.min = min

class MinStack:
    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(Node(val, val))
        else:
            n = self.stack[-1]
            if val < n.min:
                self.stack.append(Node(val, val))
            else:
                self.stack.append(Node(val, n.min))

    def pop(self) -> None:
        n = self.stack.pop()
        return n.val

    def top(self) -> int:
        n = self.stack[-1]
        return n.val

    def getMin(self) -> int:
        n = self.stack[-1]
        return n.min
'''

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
