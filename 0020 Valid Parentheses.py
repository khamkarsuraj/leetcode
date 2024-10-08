class Solution:
    def isValid(self, s: str) -> bool:
        # Using stack
        # Time: O(n)
        # Space: O(n)
        if len(s) % 2 is not 0:
            return False

        stack = []

        for i in range(0, len(s)):
            if s[i] is '(' or s[i] is '{' or s[i] is '[':
                stack.append(s[i])
            elif len(stack) is not 0:
                ch = stack.pop()
                if ch is '(' and s[i] is not ')':
                        return False
                elif ch is '{' and s[i] is not '}':
                        return False
                elif ch is '[' and s[i] is not ']':
                        return False
            else:
                return False
        
        if len(stack) is not 0:
            return False
        
        return True
