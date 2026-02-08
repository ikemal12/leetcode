class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()

        def bfs(r, c):
            q = collections.deque([r, c])
            nearestGate = 0
            while q:
                r, c = q.popleft()
                if r not in range(ROWS) or c not in range(COLS) or rooms[r][c] == -1:
                    return
                if rooms[r][c] == 0:
                    return nearestGate
                nearestGate += 1
                visit.add((r, c))
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and rooms[r][c] == float("-inf"):
                    bfs(r, c)












        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque()

        def addRoom(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visit or rooms[r][c] == -1):
                return
            visit.add((r, c))
            q.append([r, c])


        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1
