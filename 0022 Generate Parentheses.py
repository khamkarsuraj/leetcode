class Solution:
    # Using only valid combination
    # Time O(4^n / sqrt(n))
    # Space O(C(n) * 2n)        C(n): n-th Catalan number
    
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s, open, close):
            if len(s) == n*2:
                res.append(s)
                return

            # Go left with OPEN
            if open < n:
                backtrack(s + '(', open+1, close)
            # Go righ with CLOSE
            if close < open:
                backtrack(s + ')', open, close+1)

        backtrack('', 0, 0)
        return res

    '''
    # Check every possible combination
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
        '''
