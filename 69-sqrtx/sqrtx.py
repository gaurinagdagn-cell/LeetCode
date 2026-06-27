class Solution:
    def mySqrt(self, x: int) -> int:
        #binary search

        if x < 2:
            return x
        
        left, right = 2, x // 2
        
        while left <= right:
            mid = left + (right - left) // 2
            num = mid * mid
            
            if num == x:  #perfeect sqaure
                return mid
            elif num < x:  #left ptr up
                left = mid + 1
            else:  
                right = mid - 1  #right ptr down 
                
        return right
        