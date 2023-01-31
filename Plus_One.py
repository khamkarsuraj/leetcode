class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #Approach 1
        '''
        str1 = [str(i) for i in digits]
        res = int("".join(str1))
        res += 1
        str2 = [int(x) for x in str(res)]
        return str2
        '''

        #Approach 2
        if len(digits) == 0:
            return digits
        else:
            if digits[-1] != 9:
                digits[-1] += 1
                return digits
            else:
                i = -1
                haccha = False

                while((len(digits) + i > -1) and digits[i] == 9):
                    digits[i] = 0
                    i = i - 1
                    haccha = True
                
                if haccha == True and (len(digits) + i > -1) :
                    digits[i] +=1
                elif digits[0] == 0:
                    arr = [0] * (len(digits)+1)
                    arr[0] = 1
                    for i in range(1, len(arr)):
                        arr[i] = digits[i-1]
                    return arr

                return digits
