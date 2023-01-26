class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = nums.copy()
        for a, b in enumerate(nums):
            if target - b in dict and (a != dict.index(target-b)):
                return a, dict.index(target-b)
