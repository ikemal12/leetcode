class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        res = []

        def backtrack(i, j, cur, total):
            if j == k and total == n:
                res.append(cur.copy())
                return
            if i == len(nums) or j > k or total > n:
                return
            cur.append(nums[i])
            backtrack(i + 1, j + 1, cur, total + nums[i])
            cur.pop()
            backtrack(i + 1, j, cur, total)
        backtrack(0, 0, [], 0)
        return res