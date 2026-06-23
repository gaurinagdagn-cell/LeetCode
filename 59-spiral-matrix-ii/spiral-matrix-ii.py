class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        # initialize nxn matrix
        matrix = [[0] * n for _ in range(n)]
        
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        
        num = 1
        target = n * n
        
        while num <= target:
            # traverse from left to right along the top row
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1 # move the top boundary down
            
            #traverse from top to bottom along the right column
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1 # move the right boundary left
            
            #traverse from right to left along the bottom row
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1 # move the bottom boundary up
            
            # traverse from bottom to top along the left column
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1 # move the left boundary right
            
        return matrix
        