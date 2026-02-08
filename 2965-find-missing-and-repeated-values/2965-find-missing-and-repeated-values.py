class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        ans = []
        n = len(grid)
        for r in range(n):
            for c in range(n):
                if grid[r][c] in seen:
                    ans.append(grid[r][c])
                else:
                    seen.add(grid[r][c])
        ans.append(((n**2 * (n**2 + 1))//2) - sum(seen))
        return ans