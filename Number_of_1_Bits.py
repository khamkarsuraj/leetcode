class Solution:
    def hammingWeight(self, n: int) -> int:
        # Approach 1: Convert into binary and count number of 1's
        # Time Complexity: O(n) | Space Complexity: O(1)
        # return bin(n)[2:].count('1')
        
        # Approach 2: Just count number of bits for given number
        # Time Complexity: ~O(n) | Space Complexity: O(1)
        # return n.bit_count()

        # Approach 3: Simple loop
        # Time Complexity: O(n) | Space Complexity: O(1)
        counter = 0
        for i in bin(n):
            if i == '1':
                counter+=1
        return counter
