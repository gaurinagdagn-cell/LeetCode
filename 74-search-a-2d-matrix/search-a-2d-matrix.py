class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #number of rows and columns
        m = len(matrix)
        n = len(matrix[0])

        #binary search on the 1D array
        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2

            #converting the 1D index into 2D coord
            row = mid // n
            col = mid % n

            value = matrix[row][col]

            if value == target:
                return True

            elif value < target:
                left = mid + 1

            else:
                right = mid - 1

        return False
        