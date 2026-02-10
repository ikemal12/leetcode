class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap, tMap = {}, {}
        for c1, c2 in zip(s, t):
            if ((c1 in sMap and sMap[c1] != c2) or
                (c2 in tMap and tMap[c2] != c1)):
                return False
            sMap[c1] = c2
            tMap[c2] = c1
        return True
