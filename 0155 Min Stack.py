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


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
