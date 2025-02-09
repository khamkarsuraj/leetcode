class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtrack dfs
        # time n!
        # space n
        # list to return
        result = []
        n = len(nums)

        def dfs(path, used):
            # if length of path or added items are equal to
            # total number of elements then it means all
            # elements are visited so add it to the result
            if len(path) == len(nums):
                result.append(path[:])
                return

            # go iteratively for all elements
            for i in range(n):
                # to avoid duplicates if already visited
                # move to next element
                if used[i]:
                    continue
                
                # mark element visited and add to current
                # path
                used[i] = True
                path.append(nums[i])

                # now to go over all elements pass it current
                # visited path recursively
                dfs(path, used)

                # once done with nums[i] i.e. visited remove it
                # from current path to get all permutation
                # make it as not visited
                # [1, 2] which is [T, T, F] will become
                # [1] which is [T, F, F] and next combination will be
                # [1, 3] which is [T, F, T]
                path.pop()
                used[i] = False
        
        # initially no elements are visited start with all False
        dfs([], [False] * n)
        return result
