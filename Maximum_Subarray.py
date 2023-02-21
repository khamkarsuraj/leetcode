class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Approach 1: Iterate through list
        # Time Complexity: O(n) | Space Complexity: O(1)
        num = total = nums[0]        

        for i in range(1, len(nums)):
            num = max(nums[i], nums[i] + num)
            total = max(num, total)
        
        return total
