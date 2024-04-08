class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Using map
        # Time: O(n)
        # Space: O(n)
        map = {}
        n = len(nums)

        for index in range(n):
            rem = target - nums[index]
            if rem in map:
                return [map[rem], index]
            map[nums[index]] = index

        return []
        
        '''
        # Using Counter and index
        # Time: O(n^3)
        # Space: O(1)
        for i in range(0, len(nums)):
            if (nums.count(target - nums[i]) > 0 and i != nums.index(target - nums[i])):
                return [i, nums.index(target - nums[i])]
        '''
