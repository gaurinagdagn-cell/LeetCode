class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        #finding substring in the string
        if needle == "": 
            return  0

        for i in range(len(haystack) + 1 - len(needle)):  #every pos where needle can fit
            if haystack[i : i + len(needle)] == needle :   #chacks if piece of str matches needle
                return i
        return -1
        