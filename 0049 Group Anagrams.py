class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using Dictionary
        # Time O(n)
        # Space O(n)
        ans = {}
        for i in range(0, len(strs)):
            sorted_key = ''.join(sorted(strs[i]))
            if sorted_key not in ans:
                ans[sorted_key] = [strs[i]]
            else:
                ans[sorted_key].append(strs[i])

        return ans.values()
