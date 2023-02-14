class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Approach 1: Iterate through loop till we find n, return True
        # if res crosses n then return False
        # Time Complexity: O(logn) | Space Complexity: O(1)
        '''
        if n is 1:
            return True
        
        res = 1
        while res <= n:
            res = res * 2
            if res == n:
                return True
        
        return False
        '''

        # Approach 2: Checking given number in binary
        # If it has only single one return True, else False
        if n<=0:
            return False
        
        n = bin(n)
        if n.count('1', 2) == 1:
            return True
        return False
