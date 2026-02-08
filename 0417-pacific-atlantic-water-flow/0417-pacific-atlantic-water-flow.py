class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return heights
        ROWS, COLS = len(heights), len(heights[0])
        pq, aq = deque(), deque()

        for r in range(ROWS):
            pq.append((r, 0))
            aq.append((r, COLS - 1))
        for c in range(COLS):
            pq.append((0, c))
            aq.append((ROWS - 1, c))

        def bfs(q):
            reachable = set()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:
                r, c = q.popleft()
                reachable.add((r, c))
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(ROWS) and col in range(COLS) and (row, col) not in reachable and heights[row][col] >= heights[r][c]:
                        q.append((row, col))
            return reachable
        
        pac_res = bfs(pq)
        atl_res = bfs(aq)
        return list(pac_res.intersection(atl_res))


        
















        """rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or
                r < 0 or c < 0 or r == rows or c == cols or
                heights[r][c] < prevHeight):
                return

            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows-1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols-1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res"""
