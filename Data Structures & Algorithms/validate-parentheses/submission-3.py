class Solution:
    def isValid(self, s: str) -> bool:
        ourMap = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []
        for c in s:
            if c in ourMap:
                if stack and stack[-1] == ourMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False

        