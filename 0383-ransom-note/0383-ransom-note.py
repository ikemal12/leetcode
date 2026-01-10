class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countR, countM = {}, {}
        for c in ransomNote:
            countR[c] = 1 + countR.get(c, 0)
        for c in magazine:
            countM[c] = 1 + countM.get(c, 0)
        
        for c in countR:
            if c not in countM or countR[c] > countM[c]:
                return False
        return True