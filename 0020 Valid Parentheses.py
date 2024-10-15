class Solution:
    def isValid(self, s: str) -> bool:
        # Using Stack
        # Time O(n)
        # Space O(n)
        stack = deque()
        matching_brackets = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in matching_brackets.values():
                stack.append(char)
            elif char in matching_brackets:
                if not stack or stack.pop() != matching_brackets[char]:
                    return False
            else:
                return False

        return not stack
