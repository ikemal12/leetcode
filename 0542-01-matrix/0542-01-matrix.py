class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = float("inf")
        
        while q:
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(ROWS) and col in range(COLS) and mat[row][col] > mat[r][c]:
                        mat[row][col] = mat[r][c] + 1
                        q.append((row, col))
        return mat















        queue = deque()
        rows, cols = len(mat), len(mat[0])
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append((row, col))
                else:
                    mat[row][col] = float("inf")

        while queue:
            r, c = queue.popleft()
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if 0 <= row < rows and 0 <= col < cols and mat[row][col] > mat[r][c] + 1:
                    mat[row][col] = mat[r][c] + 1
                    queue.append((row, col))
        return mat