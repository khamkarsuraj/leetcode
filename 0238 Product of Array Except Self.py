class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix, Sufix Product
        # Time O(n)
        # Space (1)
        output = [0] * len(nums)
        product = 1

        # Calculate prefix product first
        for i in range(0, len(nums)):
            output[i] = product
            product = product * nums[i]
        
        product = 1
        # Now as we already have prefix calculated
        # Calculate sufix and add it to output array
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i] * product
            product = product * nums[i]

        return output

        # Brute Force Method - TLE
        # Time O(n^2)
        # Space O(n)
        '''
        output = [0] * len(nums)
        for i in range(0, len(nums)):
            prod = 1
            for j in range(0, len(nums)):
                if i != j:
                    prod = prod * nums[j]
            output[i] = prod

        return output
        '''
