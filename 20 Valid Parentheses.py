from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        if (len(s) == 1):
            return False
        elif(s[0] == ")" or s[0] == "}" or s[0] == "]"):
            return False

        for i in range(0, len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            else:
                if(len(stack)):
                    temp = stack.pop()
                else:
                    return False
                    
                if temp == "(" and s[i] != ")":
                    return False
                elif temp == "{" and s[i] != "}":
                    return False
                elif temp == "[" and s[i] != "]":
                    return False
        
        if len(stack) == 0:
            return True
        return False
