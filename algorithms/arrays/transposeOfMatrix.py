class Solution:
    def transposeMatrix(self,matrix):
        """
        :type matrix: List[List[int]]
        :rtype : List[list[int]]
        """
        rows, cols = len(matrix), len(matrix[0])
        res = [[0]* rows for _ in range(cols)]

        for r in rows:
            for c in cols:
                res[c][r] = matrix[r][c]
        return res

