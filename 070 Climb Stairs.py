class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 2

        arr = [0] * (n+1)
        arr[0] = 0
        arr[1] = 1
        arr[2] = 2

        # Followed the sequence from 1 to 5
        # Found Fabonacci series is the ans
        for i in range(3, n+1):
            arr[i] = arr[i-1] + arr[i-2]
        
        return arr[n]
