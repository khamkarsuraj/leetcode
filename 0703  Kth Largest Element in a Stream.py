import heapq

class KthLargest:
    # min-heap using heapq
    # time 
        # initialize nlogk
        # insert logk
        # search 1

    # space k
    def __init__(self, k: int, nums):
        self.k = k
        self.pq = nums
        # convert input array into min-heap
        heapq.heapify(self.pq)

        # keep only k number of elements in min-heap
        while len(self.pq) > self.k:
            heapq.heappop(self.pq)

    def add(self, val: int) -> int:
        # add new element into min-heap
        heapq.heappush(self.pq, val)

        # remove extra element to maintain min-heap
        # of size k
        while len(self.pq) > self.k:
            heapq.heappop(self.pq)

        return self.pq[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
