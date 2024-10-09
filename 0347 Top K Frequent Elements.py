class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Using Min Heap
        # Time O(nlogk)
        # Space O(n)
        # Get count of all elements
        counter = Counter(nums)
        minHeap = []
        heapify(minHeap)

        for key, val in counter.items():
            if len(minHeap) < k:
                # Push in min heap with val, key
                heapq.heappush(minHeap, (val, key))
            else:
                # if min heap is full already
                # push and pop
                # so that min val will get pop and max val stay
                heapq.heappushpop(minHeap, (val, key))
        
        return [h[1] for h in minHeap]

        # Using Dictionary
        # Time O(m+nlogn)
        # Space O(n)
        # m is length of array
        # n is no of unique elements
        '''
        ans = defaultdict(int)

        for n in nums:
            ans[n] = ans[n] + 1
        
        sorted_ans = sorted(ans.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_ans[:k]]
        '''
