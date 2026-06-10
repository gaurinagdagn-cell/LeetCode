class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # add open when open < n
        # n open and n closed paranthesis 
        # close < open then add open

        stack = []
        res = []

        def backtrack(openN , closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:  #addind open bracket
                stack.append("(")
                backtrack(openN + 1 , closedN) #updating count
                stack.pop() #popping and adding to list

            if closedN < openN:  
                stack.append(")")
                backtrack(openN , closedN + 1)
                stack.pop()

        backtrack(0 , 0)
        return res


        