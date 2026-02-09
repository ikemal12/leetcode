class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def bfs(r, c):
            q = collections.deque([(r, c)])
            visit.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            closed = True
            while q:
                r, c = q.popleft()
                if grid[r][c] == 0 and (r == 0 or r == ROWS-1 or c == 0 or c == COLS-1):
                    closed = False
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(ROWS) and col in range(COLS) and (row, col) not in visit and grid[row][col] == 0:
                        q.append((row, col))
                        visit.add((row, col))
            return closed
        
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == 0:
                    if bfs(r, c):
                        islands += 1
        return islands

        