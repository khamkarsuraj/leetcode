class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary search comparing right and middle
        # time logn
        # space 1
        l, r = 0, len(nums)-1

        while l < r:
            m = (l+r)//2
            # means left side is sorted and greater, look right side of m
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m

        return nums[r]
