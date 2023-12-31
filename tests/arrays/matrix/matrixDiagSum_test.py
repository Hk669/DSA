import unittest
from algorithms.arrays.matrix.matrixDiagSum import Solution


class TestMatrixDiagonalSum(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_matrixDiagSum(self):

        mat1 = [[1,2,3],
                [4,5,6],
                [7,8,9]]
        
        mat2 = [[1,1,1],
                [1,1,1],
                [1,1,1]]
        
        res1 = 20
        res2 = 5

        self.assetEqual(res1, self.sol.diagonalSum(mat1))
        self.assertEqual(res2, self.sol.diagonalSum(mat2))

if __name__ == '__main__':
    unittest.main()