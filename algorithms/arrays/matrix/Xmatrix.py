class Solution:
    def Xmatrix(self,matrix):
        """
        :type matrix: List[List[int]]
        :rtype :bool
        """
        r,c = len(matrix) , len(matrix[0])

        for i in range(r):
            for j in range(c):

                is_leftdiag = i==j
                is_right_diag = i+j == r-1

                if is_leftdiag or is_right_diag:
                    if matrix[i][j] == 0:
                        return False
                    
                elif matrix[i][j] != 0:
                    return False
        return True
                