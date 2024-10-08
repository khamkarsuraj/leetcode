class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's Algorithm
        # Time: O(n)
        # Space: O(1)
        
        sum = 0
        # First element always because
        # there has to atleast one element in subarray
        maximum = nums[0]

        for i in nums:
            sum = sum + i
            maximum = max(maximum, sum)
            # If there is number causes decrement in sum
            # start new sub-array
            if sum < 0:
                sum = 0
        
        return maximum
