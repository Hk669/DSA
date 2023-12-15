# 2482. Difference Between Ones and Zeros in Row and Column

class Solution:
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype : List[List[int]]
        """

        rows , cols = len(grid), len(grid[0])
        res = []
        
        # to avoid time limit , where for the huge grid it takes O(n^3)
        row_ones = [sum(row) for row in grid]
        col_ones = [sum(grid[row][j] for row in range(rows)) for j in range(cols)]

        for i in range(rows):
            onesRow = row_ones[i]
            zeroRow = cols-onesRow
            arr = []
            for j in range(cols):
                onesCol = col_ones[j]
                zeroCol = rows - onesCol

                result = self.diff(onesRow, onesCol, zeroRow, zeroCol)
                arr.append(result)
            res.append(arr)
        return res

    def diff(self,onesRow, onesCol, zeroRow, zeroCol):
        return onesRow + onesCol - zeroRow - zeroCol
    