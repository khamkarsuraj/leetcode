class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        Appraoch: Binary Search
        Time: O(logn)
        Space: O(1)
        '''
        if (len(nums) == 1):
            return 0

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left+right) // 2

            if (mid == 0 and nums[mid] > nums[mid+1]):
                return mid
            elif (mid == len(nums) - 1 and nums[mid] > nums[mid-1]):
                return mid
            elif (nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]):
                return mid

            if (nums[mid+1] > nums[mid]):
                left = mid + 1
            else:
                right = mid - 1
