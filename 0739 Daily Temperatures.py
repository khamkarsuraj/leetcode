class Node:
    def __init__(self, val, index):
        self.val = val
        self.index = index

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = deque()

        for i in range(0, len(temperatures)):
            while stack and temperatures[i] > stack[-1].val:
                ans[stack[-1].index] = i - stack[-1].index
                stack.pop()
            stack.append(Node(temperatures[i], i))

        return ans
            
