class Solution:
    def mySqrt(self, x: int) -> int:
        #Using system functions
        '''
        a = sqrt(x)
        return floor(a)
        '''

        #Using Binary Search approach
        if x < 2:
            return x
        
        start = 0
        end = x/2

        while(start <= end):
            mid = int ((start+end) / 2)
            square = mid*mid

            if square == x:
                return int(mid)
            
            if square > x:
                end = mid - 1
            else:
                start = mid + 1

        return int(end)
