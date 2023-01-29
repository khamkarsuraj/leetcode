class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums)-1
        count = 0
        i=0

        if len(nums) == 0:
            return 0

        while(i < len(nums) and nums[i] != -1):
            if nums[i] == val:
                nums[i] = nums[end]
                nums[end] = -1
                end-=1
            else:
                i+=1
                count += 1

        return count
        
        '''count = 0
        for i in nums:
            if i != val:
                nums[count] = i
                count+=1
        return count'''
