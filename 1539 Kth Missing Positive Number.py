class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Approach 1: count the numbers and return last one
        # Time Complexity: O(n) | Space Complexity: O(1)
        '''
        cnt = 0
        i = 1
        while cnt < k:
            if i not in arr:
                cnt += 1
            i += 1

        return i-1
        '''

        # Approach 2: Binary search
        # Time Complexity: O(logn) | Space Complexity: O(1)
        l, r = 0, len(arr)-1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] - (mid + 1) < k:
                l = mid + 1
            else:
                r = mid - 1
        return l + k
