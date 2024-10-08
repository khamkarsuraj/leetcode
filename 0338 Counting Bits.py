class Solution:
    def countBits(self, n: int) -> List[int]:
        # Approch 1:
        # Time Complexity: O(n) | Space Complexity: O(n)
        res = [0] * (n+1)
        for i in range(n+1):
            res[i] = bin(i).count('1')
        return res
