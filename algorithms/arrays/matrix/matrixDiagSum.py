class Solution:
    def diagonalSum(self,matrix):
        """
        :type matrix: List[List[int]]
        :rtype : int
        """
        r, c= len(matrix), len(matrix[0])
        sum = 0

        for i in range(r):
            a = matrix[i][i]
            b = matrix[i][c-i-1]
            sum += a+b
        
        if r%2 == 0:
            return sum
        else:
            m = (r+1)//2 -1
            return sum - matrix[m][m]