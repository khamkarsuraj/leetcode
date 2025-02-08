class Solution:
    def combinationSum2(self, candidates, target):
        # backtrack dfs
        # time 2^n
        # space n
        result = []
        # sorting to avoid duplicates
        candidates.sort()

        def dfs(start, path, currentSum):
            # if sum is equal to target add it into result
            # no need to look for indexes after that as all
            # sum would be greater than target, so return
            if currentSum == target:
                result.append(path[:])
                return
            
            # if sum is already greater than target return to
            # avoid unnecessary recursion for dfs
            if currentSum > target:
                return
            
            # here check for all combinations
            for i in range(start, len(candidates)):
                # if i is not starting point or index then check if it is
                # repeated value, ignore if it is
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # as value at index i is not duplicate add it into path
                path.append(candidates[i])

                # move to next index with current path and
                # new sum of existing sum + value at current index i
                dfs(i+1, path, currentSum+candidates[i])

                # here we come if sum > target or sum == target
                # basically remove recently added element
                # as it's operation is done. Undo choice
                path.pop()

        # start with 0 index
        # passing empty array as initial path
        # sum is 0
        dfs(0, [], 0)
        return result
