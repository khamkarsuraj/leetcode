class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search to look in left or right of the middle
        # comparing target exist in range of l to m and m to r
        # time logn
        # space 1
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m

            # if left is sorted
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1 
            # right is sorted
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1
