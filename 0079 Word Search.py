class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, index):
            if index == len(word):
                return True
    
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'

            found = ( 
                dfs(r-1, c, index+1) or # up
                dfs(r+1, c, index+1) or # down
                dfs(r, c+1, index+1) or # right
                dfs(r, c-1, index+1) # left
                )

            board[r][c] = temp

            return found

        for i in range(rows):
            for j in range(cols):
                if word[0] == board[i][j]:
                    if dfs(i, j, 0):
                        return True

        return False
