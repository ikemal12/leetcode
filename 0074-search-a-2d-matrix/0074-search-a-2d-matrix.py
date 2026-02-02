class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        for i in range(rows):
            l, r = 0, cols - 1
            while l <= r:
                m = (l + r) // 2
                if matrix[i][m] == target:
                    return True
                elif matrix[i][m] < target:
                    l = m + 1
                else:
                    r = m - 1
        return False