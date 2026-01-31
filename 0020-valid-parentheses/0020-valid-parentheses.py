class Solution:
    def isValid(self, s: str) -> bool:
        brackets = { "}":"{", "]":"[", ")":"("}
        stack = []

        for i in range(len(s)):
            if s[i] == "]" or s[i] == "}" or s[i] == ")":
                if stack and stack[-1] == brackets[s[i]]:
                    stack.pop()
                    continue
            stack.append(s[i])
        
        return False if stack else True
















        closeToOpen = { "}": "{", ")": "(", "]": "["}
        stack = []

        for bra in s:
            if bra in closeToOpen:
                if stack and closeToOpen[bra] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bra)
            
        return False if stack else True















        closeToOpen = { "}": "{", "]": "[", ")": "("}
        stack = []

        for c in s:
            if c in closeToOpen and stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                stack.append(c)

        return False if stack else True













        stack = []
        closeToOpen = {"}": "{", ")": "(", "]": "["}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False















        stack = []
        brackets = {')':'(', ']':'[', '}':'{'}

        for bra in s:
            #if its an opening bracket, push it to the stack
            if bra in brackets.values():
                stack.append(bra)
            else:
                # otherwise it must be a closing bracket
                # so check if its corresponding open bracket is at top of stack
                # if so pop it, otherwise return false
                if stack and stack[-1] == brackets[bra]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
        