class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search with helper function
        # time log(max(piles) * n)
        # space 1

        def cal_total_time(m: int):
            total_time = 0
            for pile in piles:
                # used ceil to round up upwards to nearest value
                total_time += math.ceil(pile/m)
            return total_time

        # assign left and right pointers to min and max speed
        l = 1
        r = max(piles)

        res = 0
        while l <= r:
            m = (l+r)//2
            # for value of m in array[l:r]
            # if she can eat bananas then mark it as solution and look for another possible/lesser m
            if cal_total_time(m) <= h:
                res = m
                r = m - 1
            # if total_time is greater than given h, means needs more speed i.e. k 
            else:
                l = m + 1

        return res
