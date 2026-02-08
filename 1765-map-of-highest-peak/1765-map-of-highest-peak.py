class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(isWater), len(isWater[0])
        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if isWater[r][c] == 1:
                    isWater[r][c] = 0
                    q.append((r, c))
                else:
                    isWater[r][c] = float("inf")
        
        while q:
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(ROWS) and col in range(COLS) and isWater[row][col] > isWater[r][c] + 1:
                        isWater[row][col] = isWater[r][c] + 1
                        q.append((row, col))
        return isWater