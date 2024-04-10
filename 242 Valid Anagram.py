class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Using ASCII encoding
        # Time: O(n)
        # Space: O(1)
        ascii_arr = [0] * 26

        for i in range(0, len(s)):
            ascii_arr[ord('z') - ord(s[i])] += 1
        
        for i in range(0, len(t)):
            ascii_arr[ord('z') - ord(t[i])] -= 1
        
        for i in ascii_arr:
            if i is not 0:
                return False
        
        return True
