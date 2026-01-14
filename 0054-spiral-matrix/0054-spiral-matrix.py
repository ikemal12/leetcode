class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1

            if not (left < right and top < bottom):
                break

            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1

            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1
        return res














        res = []
        rows, cols = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, rows-1, 0, cols-1
        while top <= bottom and left <= right:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            for j in range(top+1, bottom+1):
                res.append(matrix[j][right])
            if top < bottom:
                for i in range(right-1, left-1, -1):
                    res.append(matrix[bottom][i])
            if left < right:
                for j in range(bottom-1, top, -1):
                    res.append(matrix[j][left])
            top, bottom, left, right = top+1, bottom-1, left+1, right-1
        return res
    