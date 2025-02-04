class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking
        # time 2^n
        # space n
        result, temp_res = [], []

        def backtrack_dfs(index):
            if index == len(nums):
                result.append(temp_res.copy())
                return

            # to not to pick it up go to next index
            backtrack_dfs(index+1)

            # when you decided to pick it up, copy solution and remove latest
            # so that there won't duplicates
            temp_res.append(nums[index])
            backtrack_dfs(index+1)
            temp_res.pop()

        backtrack_dfs(0)
        return result
