class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
            
        result = []
        
        #initialize the four boundaries
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # 1 traverse from left to right alongtop row
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1
            
            # 2 traverse from top to tottom along the right column
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1
            
            # check if boundaries have crossed before moving backwards
            if top <= bottom:
                # 3 traverse from rght to left along the bottom row
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1 
                
            if left <= right:
                # 4 traverse from bottom to top along the teft column
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
                
        return result
        