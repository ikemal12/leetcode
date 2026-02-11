class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        res = maxCount = 0
        rows, cols = len(mat), len(mat[0])
        for r in range(rows):
            count = 0
            for c in range(cols):
                if mat[r][c] == 1:
                    count += 1
            if count > maxCount:
                maxCount = count
                res = r
        return [res, maxCount]















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