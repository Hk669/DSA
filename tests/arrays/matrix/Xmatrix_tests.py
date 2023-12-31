import unittest
from algorithms.arrays.matrix.Xmatrix import Solution

class XmatrixTest(unittest.TestCase):
    
    def setUp(self):
        self.sol = Solution()

    def test_Xmatrix(self):

        mat1 = [[1,0,3],
               [0,4,0],
               [3,0,9]]
        
        mat2 = [[1,0,0,1],
                [0,2,3,0],
                [0,8,6,0],
                [4,0,0,8]]
        
        mat3 = [[0,6,3],
                [0,3,0],
                [4,0,2]]

        self.assertTrue(self.sol.Xmatrix(mat1))
        self.assertTrue(self.sol.Xmatrix(mat2))

        self.assertFalse(self.sol.Xmatrix(mat3))

if __name__ == '__main__':
    unittest.main()
    