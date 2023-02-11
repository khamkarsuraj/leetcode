class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Approach 1: Sort list and check set of two numbers from start to end
        # If set of two numbers are distinct return that number, else last number of list
        # Time Complexity: O(nlogn) | Space Complexity: O(1)
        nums.sort()
        for i in range(0, len(nums)-2, 2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[len(nums)-1]

        # Approach 2: Using count
        # Time Complexity: O(n^2) | Space Complexity: O(1)
        '''
        for i in nums:
            if nums.count(i) == 1:
                return i
        '''


        # Approach 3: Using dict
        # Time Complexity: O(n) | Space Complexity: O(n)
        '''
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for i in d:
            if d[i] == 1:
                return i
        '''
