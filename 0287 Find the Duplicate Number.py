class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # using Flyod's Tortoise Hare algo
        # time n
        # space 1
        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow

        # using indexing
        # time n
        # space 1
        # for i in range(0, len(nums)):
        #     v = abs(nums[i]) - 1
        #     if (nums[v] < 0):
        #         return abs(nums[i])
        #     nums[v] = -nums[v]

        # time n
        # space n
        # m = set()
        # for i in range(0, len(nums)):
        #     if m.__contains__(nums[i]):
        #         return nums[i]
        #     m.add(nums[i])

        # time nlogn
        # space 1
        # n = len(nums)

        # for i in range(0, n-1):
        #     if nums[i] ^ nums[i+1] == 0:
        #         return nums[i]
        
