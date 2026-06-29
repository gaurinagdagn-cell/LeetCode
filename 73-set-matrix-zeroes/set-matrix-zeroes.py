class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = set()
        cols = set()

        m = len(matrix)
        n = len(matrix[0])

        #finding all zeroes
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        #set rows to zero
        for i in rows:
            for j in range(n):
                matrix[i][j] = 0

        #set columns to zero
        for j in cols:
            for i in range(m):
                matrix[i][j] = 0
        