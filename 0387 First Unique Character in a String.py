class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Approach 1: Using dictionary
        # Time Complexity: O(n) | Space Complexity: O(n)
        '''
        dic = {}
        for i in range(0, len(s)):
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1
        
        for i in dic:
            if dic[i] == 1:
                return s.index(i)

        return -1
        '''

        # Approach 2: Using count
        # Time Complexity: O(n^2) | Space Complexity: O(1)
        '''
        for i in range(0, len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1
        '''

        # Approach 3: Using in, check all alphabets before and after current alphabet
        # Time Complexity: O(n^2) | Space Complexity: O(1)
        '''
        for i in range(0, len(s)):
            if s[i] not in s[:i] and s[i] not in s[i+1:]:
                return i
        return -1
        '''

        # Approach 4:
        counter = Counter(s)
        for i in range(len(s)):
            if counter[s[i]] == 1: return i
        return -1
