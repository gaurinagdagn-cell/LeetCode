class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        # Define the search space boundaries as if it were a 1D array
        low = 0
        high = m * n - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Map the 1D index back to 2D coordinates
            row = mid // n
            col = mid % n
            
            mid_val = matrix[row][col]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False