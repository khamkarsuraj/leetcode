
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

        # Approach 6: Using dictionary
        # Time Complexity: O(n) | Space Complexity: O(n)
        dict = {}
        for i in nums:
            if i in dict:
                return True
            else:
                dict[i] = 1

        return False
