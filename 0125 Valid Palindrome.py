class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        s = s.lower()

        while left < right:
            while left < len(s)-1 and (ord(s[left]) < 97 or ord(s[left]) > 122) and (ord(s[left]) < 48 or ord(s[left]) > 57):
                left+=1

            while right >= 0 and (ord(s[right]) < 97 or ord(s[right]) > 122) and (ord(s[right]) < 48 or ord(s[right]) > 57):
                right-=1
            
            if ord(s[left]) != ord(s[right]):
                return False
            else:
                left+=1
                right-=1

        return True
