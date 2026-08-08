class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {")" : "(" , "}" : "{", "]" : "["}
        openers = []
        for b in s:
            if b in close_to_open.keys():
                if not openers or close_to_open[b] != openers[-1]:
                    return False
                else:
                    openers.pop()
            else:
                openers.append(b)


        return not openers