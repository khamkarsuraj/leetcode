class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Approach 1
        # checking for alphanumeric characters and appending to st
        st = ''.join(i for i in s if i.isalnum()).lower()
        return st == st[::-1]

        # Approach 2
        '''
        j = len(s)-1
        i = 0
        while i < len(s)-1:
            if not s[i].isalnum():
                i+=1
                continue
            elif not s[j].isalnum():
                j-=1
                continue
            elif s[i].lower() != s[j].lower():
                    return False
            j-=1
            i+=1

        return True
        '''
