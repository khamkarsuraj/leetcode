class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        # time n
        # space 1
        left = 0
        alphabetCount = [0] * 26
        maxLen = 0

        for right in range(len(s)):
            alphabetCount[ord(s[right]) - 65] += 1

            while (right-left+1) - max(alphabetCount) > k:
                alphabetCount[ord(s[left]) - 65] -= 1
                left += 1
            
            maxLen = max(maxLen, right-left+1)
        
        return maxLen
            
            
