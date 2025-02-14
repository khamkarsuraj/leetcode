class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result, temp_res = [], []

        def is_palindrome(temp_str):
            return temp_str == temp_str[::-1]

        def backtrack_dfs(index):
            if index == len(s):
                result.append(temp_res[:])
                return
            
            for i in range(index, len(s)):
                if is_palindrome(s[index:i+1]):
                    temp_res.append(s[index:i+1])
                    backtrack_dfs(i+1)
                    temp_res.pop()

        backtrack_dfs(0)
        return result
