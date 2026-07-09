class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        #initialize with -1 as base for calc valid lengths
        stack = [-1]

        ans = 0

        # traversing the string
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    #no matching '(' available
                    #set curr ')' as the new base index
                    stack.append(i)
                else:
                    # curr length of subs index - index of last unmatched bracket
                    ans = max(ans, i - stack[-1])

        return ans