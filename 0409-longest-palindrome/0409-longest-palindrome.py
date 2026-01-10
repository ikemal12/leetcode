class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = set()
        res = 0
        for char in s:
            if char in counts:
                counts.remove(char)
                res += 2
            else:
                counts.add(char)
        return res + 1 if counts else res
            
        """for i in range
            for j in ra
                if substr == reversed(substr):
                    maxl = max(maxl, len(substr))
        return maxl"""
            
        
            

















        seen = set()
        res = 0

        for c in s:
            if c in seen:
                res += 2
                seen.remove(c)
            else:
                seen.add(c)
        return res + 1 if seen else res














        seen = set()
        res = 0

        for c in s:
            if c in seen:
                seen.remove(c)
                res += 2
            else:
                seen.add(c)
        return res + 1 if seen else res

        count = defaultdict(int)
        res = 0

        for c in s:
             count[c] += 1
             if count[c] % 2 == 0:
                res += 2

        for cnt in count.values():
            if cnt % 2:
                res += 1
                break
        return res
