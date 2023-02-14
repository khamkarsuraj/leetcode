class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # Approach 1: Search whole array to find index
        # Time Complexity: O(n) | Space Complexity: O(1)
        '''
        for i in range(len(nums)):
            if nums[i] >= target:
                return i

        return (len(nums))
        '''

        # Approach 2: Binary Search
        # Time Complexity: O(logn) | Space Complexity: O(1)
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low+high)//2
            # return mid index if we found exact target value
            if nums[mid] == target:
                return mid
            # Go left
            elif nums[mid] > target:
                high = mid - 1
            # Go right
            elif nums[mid] < target:
                low = mid + 1

        return low
