import unittest
from algorithms.arrays.matrix.setZeroes import Solution

class TestSetZeroes(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_setZeroes(self):
        """
        An unittest to test if the solution for the setZeroes is efficient
        - the solution makes the rows and cols of the element which is 0
        - if [1,2] is 0 -> then all the elements in row 1 and col 2 should be set to zeroes
        """

        mat1 = [[1,2,3],
               [3,5,0],
               [2,9,0]]
        
        mat2 = [[1,2,3],
               [3,0,8],
               [2,9,6]]
        
        
        result1 = [[1,2,0],
                   [0,0,0],
                   [0,0,0]]
        
        res2 = [[1,0,3],
                [0,0,0],
                [2,0,6]]


        self.assertEqual(result1, self.sol.setZeroes(mat1))
        self.assertEqual(res2, self.sol.setZeroes(mat2))
        

if __name__ == '__main__':
    unittest.main()
