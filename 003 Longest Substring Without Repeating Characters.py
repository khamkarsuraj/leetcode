class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # time n
        # space k where k is length of max substring
        unique = set()
        l = r = 0
        n = len(s)
        maxLen = 0

        while r < n:
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            else:
                unique.add(s[r])
                if maxLen < (r-l+1):
                    maxLen = r-l+1
            r += 1
        
        return maxLen
