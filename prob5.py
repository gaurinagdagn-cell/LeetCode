class Solution:
    def longestPalindrome(self, s: str) -> str:
        res= ""
        resLen= 0
        
        for i in range(len(s)):
            #eg 1
            l ,r = i ,i
            while l >= 0 and r < len(s) and s[l]==s[r]:  # going outwards from mid and checking if l and r are same
                if (r-l+1) > resLen:
                    res=s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r +=1

            #edge case even
            l ,r = i ,i+1
            while l >= 0 and r < len(s) and s[l]==s[r]:  # going outwards from mid and checking if l and r are same
                if (r-l+1) > resLen:
                    res=s[l:r+1]
                    resLen = r-l+1
                l -= 1
                r +=1
        return res


            