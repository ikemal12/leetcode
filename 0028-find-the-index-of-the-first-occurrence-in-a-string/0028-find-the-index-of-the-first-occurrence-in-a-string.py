class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack): return -1
        found = False
        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                if needle[j] != haystack[j+i]:
                    break
                if j == len(needle) - 1: 
                    found = True
            if found:
                return i
            
        return -1















        if needle == "":
            return 0

        for i in range(len(haystack) + 1 - len(needle)):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1