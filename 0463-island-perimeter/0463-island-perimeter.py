class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()

        def dfs(r, c):
            nonlocal perimeter
            if (r, c) in seen:
                return
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == 0:
                perimeter += 1
                return
            seen.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        perimeter = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r, c)
        return perimeter
            