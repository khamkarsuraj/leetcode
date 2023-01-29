class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums)-1
        count = 0

        if len(nums) == 0:
            return 0

        while(start < len(nums) and nums[start] != -1):
            if nums[start] == val:
                nums[start] = nums[end]
                nums[end] = -1
                end-=1
            else:
                start+=1
                count+= 1

        return count
        
        '''count = 0

        for i in nums:
            if i != val:
                nums[count] = i
                count+=1

        return count'''
