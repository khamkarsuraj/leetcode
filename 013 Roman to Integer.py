class Solution:
    def romanToInt(self, str):
        total = 0
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        for i in range(0, len(str)-1):
            if (roman[str[i]] < roman[str[i+1]]):
                total = total - roman[str[i]]
            else:
                total = total + roman[str[i]]
        
        total = total + roman[str[len(str)-1]]
        return total
