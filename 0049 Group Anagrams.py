class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using Array
        # Time O(mn)
        # Space O(n)
        # n number of strings
        # m average length of string
        ans = defaultdict(list)

        for s in strs:
            charArray = [0] * 26

            for char in s:
                charArray[ord(char) - ord('a')] += 1

            ans[tuple(charArray)].append(s)

        return ans.values()

        # Using Dictionary
        # Time O(nklogk)
        # Space O(nk)
        # n number of strings
        # k average length of string
        '''
        ans = {}
        for i in range(0, len(strs)):
            sorted_key = ''.join(sorted(strs[i]))
            if sorted_key not in ans:
                ans[sorted_key] = [strs[i]]
            else:
                ans[sorted_key].append(strs[i])

        return ans.values()
        '''
