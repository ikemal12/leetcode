class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length, found = 0, False
        for i in range(len(s)-1, -1, -1):
            if not found and s[i] != " ":
                found = True
            
            if found:
                if s[i] != " ":
                    length += 1
                else:
                    break
        return length



        """
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

        return length"""