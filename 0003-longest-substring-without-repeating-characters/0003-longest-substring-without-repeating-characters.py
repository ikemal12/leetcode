class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxL = 0
        l = r = 0

        while r < len(s):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            maxL = max(maxL, r - l + 1)
            seen.add(s[r])
            r += 1
        return maxL

        """
        "dvdf"
          l
             r
         seen = [v, d, f]
         maxL = 3
        """
                




















        l = 0
        seen = set()
        maxL = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxL = max(maxL, r - l + 1)
        return maxL

















        chars = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, r - l + 1)

        return res

















        chars = set()
        l = 0
        count = 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            count = max(count, r - l + 1)
        return count















        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res














        # O(n), O(n)
        seen = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r - l + 1)
        return res


















        # sliding window
        seen = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, r - l + 1)
        return res
        
        # brute force check every possible substring
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if len(s[i:j+1]) == len(set(s[i:j+1])):
                    res = max(res, len(s[i:j+1]))
        return res
            


















        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res