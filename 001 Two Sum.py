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
