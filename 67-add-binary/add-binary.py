class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        
        #ptrs starting at the back
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            #adding digit from str'a' if ptr is valid
            if i >= 0:
                total += int(a[i])
                i -= 1
                
            #adding digit from str'b' if ptr is valid
            if j >= 0:
                total += int(b[j])
                j -= 1
                
            result.append(str(total % 2))
            
            carry = total // 2
            
        # reverse string as we appended from rigth to left
        return "".join(reversed(result))