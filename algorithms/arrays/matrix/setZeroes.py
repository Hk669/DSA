class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype : List[List[int]]
        """

        r, c = len(matrix), len(matrix[0])
        zero_r , zero_c = set(), set()

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    zero_r.add(i)
                    zero_c.add(j)

        for row in zero_c:
            for col in range(c):
                matrix[row][col] = 0
        
        for row in range(r):
            for col in zero_c:
                matrix[row][col] = 0

        return matrix