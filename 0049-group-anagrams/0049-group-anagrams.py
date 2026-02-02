class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord("a")] += 1

            counts = tuple(counts)
            
            if counts in res:
                res[counts].append(s)
            else:
                res[counts] = [s]
        
        return list(res.values())
            















        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            groups[tuple(count)].append(s)
        return list(groups.values())













        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())


        groups = {}
        for s in strs:
            countS = {}
            for c in s:
                countS[c] = 1 + countS.get(c, 0)
            if countS in groups.keys():
                groups[countS].append(s)
            else:
                groups[countS] = [s]
        
        return [group for group in groups.values()]


        def validAnagram(s, t):
            countS, countT = {}, {}
            for c in s:
                countS[c] = 1 + countS.get(c, 0)
            for c in t:
                countT[c] = 1 + countT.get(c, 0)
            for c in countS:
                if countS[c] != countT[c]:
                    return False
            return True



















        hashmap = defaultdict(list) # charCount -> list of anagrams

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            hashmap[tuple(count)].append(s)
        return list(hashmap.values())






















        # brute force, sorting, O(m * nlogn)
        hashmap = {} # key: sorted string, value: list of anagrams

        for s in strs:
            key = "".join(sorted(s)) # sorting O(nlogn)
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(s)

        return list(hashmap.values())
        
        # hashmap
        res = defaultdict(list) # mapping charCount to list of anagrams
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        return res.values()


        















        sortedstrs = []
        for i in range(len(strs)):
            sortedstrs.append(' '.join(sorted(strs[i])))
        
        anagrams = {}
        for i in range(len(strs)):
            if sortedstrs[i] not in anagrams.keys():
                anagrams[sortedstrs[i]] = []
            anagrams[sortedstrs[i]].append(strs[i])
        
        res = []
        for key in anagrams.keys():
            res.append(anagrams[key])
        return res