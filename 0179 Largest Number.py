class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Using sorted method and custom comparator 
        # Time O(nlogn)
        # Space O(n)

        # Convert int to str
        for i, n in enumerate(nums):
            nums[i] = str(n)

        # compare n1 and n2
        # if n1 = 3 and n2 = 30
        # n1+n2 (330) > n2+n1 (303) so return n1 (3)
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            return 1

        ret = sorted(nums, key=cmp_to_key(compare))

        return str(int("".join(ret)))
