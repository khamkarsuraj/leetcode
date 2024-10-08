class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Approach 1: Take distinct elements into another list
        #             And count the number of occurances in original list
        # Time Complexity: O(n) | Space Complexity: O(n)
        '''
        l = list(set(nums))
        max = 0
        ele = nums[0]
        for i in l:
            s = nums.count(i)
            if s > max:
                ele = i
                max = s
        return ele
        '''

        # Approach 2: Using sort
        # Time Complexity: O(nlogn) | Space Complexity: O(1)
        '''
        nums.sort()
        return nums[len(nums)//2]
        '''

        # Approach 3: Using Boyer Moore Algorithm
        # Time Complexity: O(n) | Space Complexity: O(1)
        vote = 0 # to count votes
        var = -1 # As n will be 1 <= n always
        for i in range(0, len(nums)):
            if vote == 0:
                var = nums[i]
            
            if var == nums[i]:
                vote += 1
            else:
                vote += -1
        
        # here we have assumed that there will be always majority element present
        # if assumtion fails then we have to check that var is present in list with
        # N//2 occurances using another loop of O(n)
        return var
