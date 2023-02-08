class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        op = ''
        while len(b)<len(a):
            b='0'+b
        while len(a)<len(b):
            a='0'+a

        for i in range(len(a)-1, -1, -1):
            if int(a[i]) + int(b[i]) == 0:
                if carry == 1:
                    op = '1' + op
                    carry = 0
                else:
                    op = '0' + op
            elif int(a[i]) + int(b[i]) == 1:
                if carry == 1:
                    op = '0' + op
                    carry = 1
                else:
                    op = '1' + op
            elif int(a[i]) + int(b[i]) > 1:
                if carry == 1:
                    op = '1' + op
                else:
                    op = '0' + op
                carry = 1
        
        if carry == 1:
            op = '1' + op
        
        return op
