class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        c2W, W2c = {}, {}
        s = s.split()
        if len(pattern) != len(s): return False
        for i in range(len(pattern)):
            if ((pattern[i] in c2W and c2W[pattern[i]] != s[i]) or
                (s[i] in W2c and W2c[s[i]] != pattern[i])):
                return False
            c2W[pattern[i]] = s[i]
            W2c[s[i]] = pattern[i]
        return True
