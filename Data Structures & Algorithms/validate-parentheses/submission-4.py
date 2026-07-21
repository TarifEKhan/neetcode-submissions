class Solution:
    def isValid(self, s: str) -> bool:
        valid_dict = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for c in s:
            if c in valid_dict:
                if stack and stack[-1] == valid_dict[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False