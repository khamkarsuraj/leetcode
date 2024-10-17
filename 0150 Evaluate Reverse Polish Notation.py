class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Using Stack
        # Time O(n)
        # Space O(n)
        stack = deque()
        valid = ['+', '-', '*', '/']

        for i in tokens:
            if i in valid:
                r, l = stack.pop(), stack.pop()
                if i == '+':
                    res = l + r
                elif i == '-':
                    res = l - r
                elif i == '*':
                    res = l * r
                else:
                    res = int(l/r)
                stack.append(res)
            else:
                stack.append(int(i))

        return stack.pop() 
