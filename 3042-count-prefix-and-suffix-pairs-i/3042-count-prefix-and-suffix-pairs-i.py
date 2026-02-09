class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(w1, w2):
            n = len(w1)
            return w1 == w2[:n] and w1 == w2[-n:]

        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    res += 1
        return res

    
