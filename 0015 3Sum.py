class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Two Pointers keeping one element as threshold
        # Time O(n^2)
        # Space O(k) where k are the triplets

        nums.sort()
        res = []

        for i in range(0, len(nums)):
            # If first element after sorting is positive then sum will be positive
            # ignore in that case and return empty list
            if nums[i] > 0:
                break
            # To avoid duplicates ignore already checked nums[i]
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1

            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if three_sum == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    # To avoid duplicates
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                    while j < k and nums[k] == nums[k+1]:
                        k-=1    
                elif three_sum < 0:
                    j+=1
                else:
                    k-=1

        return res
