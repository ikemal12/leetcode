class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length, startIdx = 0, 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                startIdx = i
                break
        
        for i in range(startIdx, -1, -1):
            if s[i] == " ":
                break
            else:
                length += 1

        return length