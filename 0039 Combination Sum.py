class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # dfs backtrack
        # time 2^n
        # space n
        result = []

        def backtrack_dfs(index, path, currentSum):
            if currentSum == target:
                result.append(path[:])
                return

            if currentSum > target: # early termination of path
                return

            for i in range(index, len(candidates)):
                path.append(candidates[i])
                backtrack_dfs(i, path, currentSum + candidates[i])
                path.pop()

        backtrack_dfs(0, [], 0)
        return result
