class Solution:
    def climbStairs(self, n: int) -> int:
        #reaching last step : 1 step from n-1 step or 2 steps from n-2 step

        if n <= 2:
            return n
        
        first = 1
        second = 2
        
        #calculate ways for steps 3 up to n
        for _ in range(3, n + 1):
            current = first + second
            first = second
            second = current
            
        return second
        