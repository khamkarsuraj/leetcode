class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Refer Java solution for explanation
        pro = 1
        res = [0] * len(nums)
        
        for i in range(0, len(nums)):
            res[i] = pro
            pro = res[i] * nums[i]
        
        pro = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = pro * res[i]
            pro = pro * nums[i]
        
        return res
            
