class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {"2": "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz" }
        
        def backtrack(i, currStr, res): 
            if len(currStr) == len(digits):
                res.append(currStr)  # to add item in list
                return
            
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, currStr + c, res) #recursive
                
        if digits:
            backtrack(0, "", res) # Passed res here
            
        return res