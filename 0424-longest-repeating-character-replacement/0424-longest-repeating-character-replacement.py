class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = maxL = 0
        counts = {}
        maxf = 0

        for r in range(len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            maxf = max(maxf, counts[s[r]])
            if (r - l + 1) - maxf <= k:
                maxL = max(maxL, r - l + 1)
            else:
                counts[s[l]] -= 1
                l += 1
        return maxL

        """
        "ABAB"
        len - maxChar <= k 
        """

            














        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
        
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res















        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res

        # brute force
        # check every possible substring if it is valid and if it is update maxLen
        res = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                # check if the substring is valid
                valid = self.isValidSubstring(s[i:j+1], k)
                if valid[0]:
                    res = max(res, valid[1])
        return res

    def isValidSubstring(self, s, k):
        # get the character with highest frequency
        # num replacements = len of substring - highest freq char
        counts = self.countFrequencies(s)
        highestFreq = max(counts.values())
        numR = len(s) - highestFreq
        return (True, len(s)) if numR <= k else (False, len(s))

    def countFrequencies(self, s):
        counts = {}
        for i in range(len(s)):
            counts[s[i]] = counts.get(s[i], 0) + 1
        return counts
