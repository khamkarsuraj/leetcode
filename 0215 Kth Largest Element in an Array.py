import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Approach 2
        # time nlogk
        # space k
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
        
        return min_heap[0]

        # Approach 1
        # heapq.heapify(nums)

        # while len(nums) > k:
        #     heapq.heappop(nums)
        
        # return nums[0]
