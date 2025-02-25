class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # max heap
        # time nlogk
        # space k
        max_heap = []

        for i, (x, y) in enumerate(points):
            distance = x**2 + y**2
            heapq.heappush(max_heap, (-distance, x, y))
            while len(max_heap) > k:
                heapq.heappop(max_heap)

        return [[x, y] for _, x, y in max_heap]
