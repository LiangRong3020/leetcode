class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        col= len(matrix)
        row= len(matrix[0])

        record_col= set()
        record_row= set()

        for i in range(col):
            for j in range(row):
                if matrix[i][j] == 0:
                    record_col.add(i)
                    record_row.add(j)

        for i in range(col):
            for j in range(row):
                if i in record_col or j in record_row:
                    matrix[i][j] = 0

        return matrix
