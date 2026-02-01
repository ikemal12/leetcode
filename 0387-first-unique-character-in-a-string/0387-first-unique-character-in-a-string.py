class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = {}
        for i, char in enumerate(s):
            if char not in counts:
                counts[char] = [1, i]
            else:
                counts[char][0] += 1
        
        first = len(s) 
        for count, idx in counts.values():
            if count == 1 and idx < first:
                first = idx
        return -1 if first == len(s) else first















        counts = [0] * 26

        for c in s:
            counts[ord(c) - ord("a")] += 1
        
        for i, c in enumerate(s):
            if counts[ord(c) - ord("a")] == 1:
                return i
        return -1



       


        















        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1
        