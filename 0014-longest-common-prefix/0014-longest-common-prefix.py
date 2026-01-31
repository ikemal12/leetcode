class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                    return "".join(res)
            res.append(strs[0][i])
        return "".join(res)
            



        """if len(strs) == 1: return strs[0]

        longestP = ""
        for i in range(len(strs)):
            for j in range(i, len(strs)):
                prefix = ""
                for k in range(min(len(strs[i]), len(strs[j]))):
                    if strs[i][k] != strs[j][k]:"""
        




















        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res