class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1, t1 = [0] * 26, [0] * 26
        for char in s:
            s1[ord(char) - ord("a")] += 1
        for char in t:
            t1[ord(char) - ord("a")] += 1
        return s1 == t1


        s1, t1 = {}, {}
        for char in s:
            s1[char] = 1 + s1.get(char, 0)
        for char in t:
            t1[char] = 1 + t1.get(char, 0)
        return s1 == t1















        set1 = {}
        for char in s:
            set1[char] = 1 + set1.get(char, 0)
        
        set2 = {}
        for char in t:
            set2[char] = 1 + set2.get(char, 0)

        return True if set1 == set2 else False




















        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # go through each corresponding count
        # check if not equal -> return False
        # return countS == countT (naive approach)

        for char, count in countS.items():
            if count != countT.get(char, 0):
                return False
        return True


        

        

        













        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True















        o = [0] * 26
        for char in s:
            o[ord(char) - ord("a")] += 1
        
        p = [0] * 26
        for char in t:
            p[ord(char) - ord("a")] += 1
        
        return o == p