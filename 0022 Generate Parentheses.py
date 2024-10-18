class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = set()
        s = ''

        def valid_string(string):
            stack = deque()
            for s in string:
                if s == '(':
                    stack.append(s)
                elif stack and s == ')':
                    stack.pop()
                else:
                    return False
            return not stack
    
        def backtrack(s):
            if len(s) == n*2:
                if valid_string(s):
                    res.add(s)
                return

            # Go left with OPEN
            if s.count('(') < n:
                backtrack(s + '(')
            # Go righ with CLOSE
            if s.count(')') < n:
                backtrack(s + ')')

        backtrack(s)
        return list(res)
