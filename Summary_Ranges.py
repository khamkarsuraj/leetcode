class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # Approach 1: Iterate the list and append to resulting list accordingly
        # Time Complexity: O(n) | Space Complexity: O(1)
        if len(nums) == 0:
            return []

        start = 0
        end = 0
        res = []

        while end < len(nums):
            if end != 0 and nums[end]-nums[end-1] != 1:
                if end-start == 1:
                    strng = str(nums[start])
                else:
                    strng = str(nums[start]) + '->' + str(nums[end-1])
                res.append(strng)
                start = end
                end += 1
            else:
                end += 1
        
        if start < len(nums)-1:
            strng = str(nums[start]) + '->' + str(nums[end-1])
            res.append(strng)
        else:
            res.append(str(nums[start]))
        
        return res
