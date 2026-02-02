class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n - 1
        while l <= r:
            pivot = l + (r - l) // 2
            elem = matrix[pivot // n][pivot % n]
            if elem == target:
                return True
            elif elem < target:
                l = pivot + 1
            else:
                r = pivot - 1
        return False


        """
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
        return False"""