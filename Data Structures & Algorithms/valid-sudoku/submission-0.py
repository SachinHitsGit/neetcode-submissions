class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()
            for i in range(9):
                cur = board[row][i]
                if cur == '.':
                    continue
                if cur in seen:
                    return False
                seen.add(cur)
        for col in range(9):
            seen = set()
            for i in range(9):
                cur = board[i][col]
                if cur == '.':
                    continue
                if cur in seen:
                    return False
                seen.add(cur)
        
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square %3) * 3 + j
                    cur = board[row][col]
                    if cur == '.':
                        continue
                    if cur in seen:
                        return False
                    seen.add(cur)
        return True