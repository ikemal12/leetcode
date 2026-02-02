class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] in s:
                    return False
                if board[i][j] != ".":
                    s.add(board[i][j])

        # check columns
        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i] in s:
                    return False
                if board[j][i] != ".":
                    s.add(board[j][i])

        # check 3x3 boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s = set()
                for m in range(i, i + 3):
                    for n in range(j, j + 3):
                        if board[m][n] in s:
                            return False
                        if board[m][n] != ".":
                            s.add(board[m][n])
        return True
                        