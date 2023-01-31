class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str1 = [str(i) for i in digits]
        res = int("".join(str1))
        res += 1
        str2 = [int(x) for x in str(res)]
        return str2
