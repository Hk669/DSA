import unittest
from algorithms.arrays.matrix.transposeOfMatrix import Solution

class TestTransposeMatrix(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_transpose(self):

        mat1 = [[1,2,3],
                [4,5,6],
                [7,8,9]]
        
        mat2 = [[1,2,3],
                [2,4,5],
                [3,5,6]]
        
        res1 = [[1,4,7],
                [2,5,8],
                [3,6,9]]

        res2 = [[1,2,3],
                [2,4,5],
                [3,5,6]] 
        
        self.assertEqual(res1, self.sol.transposeMatrix(mat1))
        self.assertEqual(res2, self.sol.transposeMatrix(mat2))
        
        
if __name__ == '__main__':
    unittest.main()
    