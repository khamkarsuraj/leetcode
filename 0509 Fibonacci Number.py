class Solution:
    def fib(self, n: int) -> int:
        # dynamic programming (memoization)
        # time n
        # space n
        memo = [0] * (n+1)

        def dfs(n, memo):
            if n == 0 or n == 1:
                return n
            
            if memo[n] == 0:
                memo[n] = dfs(n-1, memo) + dfs(n-2, memo) 

            return memo[n]
        
        return dfs(n, memo)

        # Simple iterative approach
        # time n
        # space 1
        # if n == 0:
        #     return n

        # a, b = 0, 1

        # for i in range(2, n):
        #     c = a + b
        #     a = b
        #     b = c
        
        # return a+b
