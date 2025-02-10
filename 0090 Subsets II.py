class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # backtrack dfs
        # time 2^n
        # space n
        result = []
        n = len(nums)
        # sort list to avoid duplicates in loop below
        nums.sort()

        def dfs(start, path):
            result.append(path[:])
            
            # reached last element means
            # no more elements to add so return 
            if index >= n:
                return
            
            # as list is sorted start with index
            # passed previous dfs
            for i in range(start, n):
                # if i is greater than start element and
                # it is same as i-1, ignore it to avoid
                # duplicates
                if i > index and nums[i] == nums[i-1]:
                    continue
                
                # choose the number
                path.append(nums[i])

                # move to next element with current path
                dfs(i+1, path)

                # backtrack
                path.pop()

        dfs(0, [])
        return result
