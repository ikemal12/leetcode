class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ROWS, COLS = len(mat), len(mat[0])
        maxOnes, idx = 0, 0

        for i in range(ROWS):
            rowCount = 0
            for j in range(COLS):
                if mat[i][j] == 1:
                    rowCount += 1
            if rowCount > maxOnes:
                maxOnes = rowCount
                idx = i

        return [idx, maxOnes]