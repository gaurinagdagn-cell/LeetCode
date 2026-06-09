class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(" , "}" : "{" , "]" : "["}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]: #matching paranthesis
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False  #empty stack = all brackets are closed
                                             # stack not empty = bracket left open



        
        