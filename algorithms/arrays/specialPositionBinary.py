#1582
class Solution:
    def specialPos(self,matrix):
        """
        :type matrix: List[List[int]]
        :rtype : int
        """
        rows , cols = len(matrix), len(matrix[0])
        special = 0

        for i in range(rows):
            for j in range(cols):

                if matrix[i][j] == 1:
                    if sum(matrix[i]) == 0:
                        if sum(matrix[row][j] for row in range(rows)) == 1:
                            special +=1
        return special

# TestCase
# Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
# Output: 1
# Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.