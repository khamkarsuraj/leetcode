class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        # time logn
        # space 1
        l, r = 0, len(nums)-1
        while l <= r:
            m = (r+l)//2
            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m+1
            else:
                r = m-1
        return -1

        # # loop
        # # time n
        # # space 1
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1
