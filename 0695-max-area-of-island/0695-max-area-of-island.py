class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        ROWS, COLS = len(grid), len(grid[0])
        maxA = 0

        def bfs(r, c):
            nonlocal maxA
            q = collections.deque([(r, c)])
            grid[r][c] = 0

            area = 0
            while q:
                r, c = q.popleft()
                area += 1
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(ROWS) and col in range(COLS) and grid[row][col] == 1:
                        q.append((row, col))
                        grid[row][col] = 0
            maxA = max(maxA, area)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    bfs(r, c)
        return maxA















        rows, cols = len(grid), len(grid[0])
        visit = set()
        area = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visit.add((r, c))

            curr = 1
            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == 1 and
                        (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))
                        curr += 1
            return curr

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c ) not in visit:
                    area = max(area, bfs(r, c))
        return area