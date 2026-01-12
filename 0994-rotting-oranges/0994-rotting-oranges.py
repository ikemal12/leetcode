class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0

        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r+dr, c+dc
                    if (row<0 or row==ROWS or col<0 or col==COLS
                        or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -=1
            time += 1
        return time if fresh == 0 else -1





















        rows, cols = len(grid), len(grid[0])
        rotten = collections.deque()
        time, fresh = 0, 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append([r, c])
                if grid[r][c] == 1:
                    fresh += 1

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while rotten and fresh > 0:
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for dr, dc in directions:
                    if ((r + dr) in range(rows) and 
                        (c + dc) in range(cols) and
                        grid[r+dr][c+dc] == 1):
                        grid[r+dr][c+dc] = 2
                        rotten.append([r+dr, c+dc])
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
