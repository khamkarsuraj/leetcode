class Solution:
    def longestCommonPrefix(self, strs):
        # Find shortest string in list strs.
        # Compare that with all the elements from strs, return whatever you have found in common
        # else it will return empty string if nothing common found
        # Time complexity: O(n) | Space Complexity: O(1)
        if not strs:
            return ""

        shortest = min(strs,key=len)

        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]

        return shortest
