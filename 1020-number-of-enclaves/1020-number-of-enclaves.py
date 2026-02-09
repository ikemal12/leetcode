class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        visit = set()

        for r in range(ROWS):
            if grid[r][0] == 1:
                q.append((r, 0))
                grid[r][0] = 2
            if grid[r][COLS - 1] == 1:
                q.append((r, COLS - 1))
                grid[r][COLS - 1] = 2
        
        for c in range(COLS):
            if grid[0][c] == 1:
                q.append((0, c))
                grid[0][c] = 2
            if grid[ROWS - 1][c] == 1:
                q.append((ROWS - 1, c))
                grid[ROWS - 1][c] = 2

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if row in range(ROWS) and col in range(COLS) and (row, col) not in visit and grid[row][col] == 1:
                    grid[row][col] = 2
                    q.append((row, col))
                    visit.add((row, col))
        
        cells = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    cells += 1
        return cells

                

        
