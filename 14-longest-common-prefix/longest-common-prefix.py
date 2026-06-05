class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        res = ""
        
        for i in range(len(strs[0])):
            for s in strs:
                # Check if 'i' is out of bounds for the current string 's'
                # OR if the characters don't match
                if i >= len(s) or s[i] != strs[0][i]:
                    return res
            
            res += strs[0][i]
            
        return res