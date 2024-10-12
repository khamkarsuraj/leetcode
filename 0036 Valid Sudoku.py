class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = defaultdict(set)
        c = defaultdict(set)
        box = defaultdict(set)

        for i in range(0, 9):
            for j in range(0, 9):
                ele = board[i][j]
                if ele == '.':
                    continue

                if ele in r[i] or ele in c[j] or ele in box[(i//3, j//3)]:
                    return False

                r[i].add(ele)
                c[j].add(ele)
                box[(i//3, j//3)].add(ele)
        
        return True
