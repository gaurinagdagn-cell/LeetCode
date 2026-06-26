class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        #initialize a 1D array reep curr row
        row = [1] * n
        
        #looping thru the remaining rows
        for i in range(1, m):
            for j in range(1, n):
                #new value at row[j] is its current value from theabove row
                row[j] += row[j-1]
                
        return row[-1]
        