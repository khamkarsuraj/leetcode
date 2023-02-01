class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #Approach 1
        '''
        arr = s.split()
        return len(arr[-1])
        '''

        #Approach 2
        return len(s.strip().split()[-1])
