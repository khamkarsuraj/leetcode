
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Insertion Sort
        # Time: O(n^2)
        # Space: O(1)
    
        i = 0
        while i < len(nums):
            j = i - 1
            # This logic is to find index for ith element and
            # place it at its perfect index
            while j>=0 and nums[j]>nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                i -= 1
            
            # This is additional condition into Insertion sort,
            # to check into if there is duplicate element present
            # or not
            if j>= 0 and nums[j]==nums[j+1]:
                return True

            i += 1
        
        return False

        # Approach 1: Using sort method
        # Time Complexity: O(nlogn) | Space Complexity: O(1)
        '''
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        
        return False
        '''

        # Approach 3: Using default dictionary
        # Time Complexity: O(n) | Space Complexity: O(n)
        '''
        dic = defaultdict(int)  
        for i in nums:
            dic[i] += 1
            if dic[i] > 1:
                return True

        return False
        '''

        # Approach 5: Using set and list length
        # Time Complexity: O(n) | Space Complexity: O(n)
        '''
        return not len(set(nums)) == len(nums)
        '''
        '''
        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        
        return False
        '''

        # Approach 6: Using dictionary
        # Time Complexity: O(n) | Space Complexity: O(n)
        '''
        dict = {}
        for i in nums:
            if i in dict:
                return True
            else:
                dict[i] = 1

        return False
        '''
