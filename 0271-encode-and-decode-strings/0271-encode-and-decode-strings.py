class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ""
        for s in strs:
            res += s.replace("/", "//") + "/:"
        return res
        """res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res"""
        """return 'π'.join(strs)"""

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        cur = ""
        i = 0
        while i < len(s):
            if s[i:i+2] == "/:":
                res.append(cur)
                cur = ""
                i += 2
            elif s[i:i+2] == "//":
                cur += "/"
                i += 2
            else:
                cur += s[i]
                i += 1
        return res
        """"res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
        return res"""

        """return s.split('π')"""
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))