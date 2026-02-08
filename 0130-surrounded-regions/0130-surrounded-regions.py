class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        q = collections.deque()
        visit = set()

        for r in range(ROWS):
            if board[r][0] == "O":
                q.append((r, 0))
                board[r][0] = "."
            if board[r][COLS - 1] == "O":
                q.append((r, COLS - 1))
                board[r][COLS - 1] = "."
        for c in range(COLS):
            if board[0][c] == "O":
                q.append((0, c))
                board[0][c] = "."
            if board[ROWS - 1][c] == "O":
                q.append((ROWS - 1, c))
                board[ROWS - 1][c] = "."
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row in range(ROWS) and col in range(COLS) and board[row][col] == "O" and (row, col) not in visit:
                    board[row][col] = "."
                    q.append((row, col))
                    visit.add((row, col))
            
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == ".":
                    board[r][c] = "O"

                
                












        """#next time solve with constant space (hint: no need for a set)
        rows, cols = len(board), len(board[0])
        unusable = set()

        def dfs(r, c, visit, prevCell):
            if (r < 0 or c < 0 or r == rows or c == cols
                or (r, c) in unusable or board[r][c] == "X"):
                return
            unusable.add((r,c))
            dfs(r+1, c, unusable, board[r][c])
            dfs(r-1, c, unusable, board[r][c])
            dfs(r, c+1, unusable, board[r][c])
            dfs(r, c-1, unusable, board[r][c])

        for r in range(rows):
            dfs(r, 0, unusable, board[r][0])
            dfs(r, cols-1, unusable, board[r][cols-1])
        
        for c in range(cols):
            dfs(0, c, unusable, board[0][c])
            dfs(rows-1, c, unusable, board[rows-1][c])

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in unusable and board[r][c] == "O":
                    board[r][c] = "X"
                    """
                
        