class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxl = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxl:
                    maxl = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxl:
                    maxl = r - l + 1
                    res = s[l:r+1]
                l -= 1
                r += 1
        return res
        
        
            

















        # two pointer
        def isPali(l, r):
            return s[l:r+1] == s[l:r+1][::-1]

        maxLen = 0
        res = ""
        n = len(s)

        for i in range(len(s)):
            # odd length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    res = s[l:r+1]
                    maxLen = r - l + 1
                l -= 1
                r += 1
            # even length palindromes
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    res = s[l:r+1]
                    maxLen = r - l + 1
                l -= 1
                r += 1
        return res

        # brute force
        maxLen = 0
        res = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    if (j - i + 1) > maxLen:
                        maxLen = j - i + 1
                        res = s[i:j+1]
        return res

        














        def isPali(s):
            return (s == s[::-1])

        # brute force solution
        """res = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPali(s[i:j+1]) and len(s[i:j+1]) > len(res):
                    res = s[i:j+1]
        return res"""

        def expandAroundCenter(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]

        res = ""
        for i in range(len(s)):
            s1 = expandAroundCenter(i, i)
            s2 = expandAroundCenter(i, i+1)
            if len(s1) > len(res):
                res = s1
            if len(s2) > len(res):
                res = s2
        return res
