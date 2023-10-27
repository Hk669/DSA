from algorithms.arrays.three_sum import Solution
import unittest

class threeSumTest(unittest.TestCase):

    def test_threesum1(self):

        solution = Solution()
        nums = [-1,0,1,2,-1,-4]

        result = solution.threesum(nums)
        self.assertEqual(result, [[-1,-1,2],[-1,0,-1]])

    def test_threesum2(self):

        solution = Solution()
        nums = [0,1,1]

        result = solution.threesum(nums)
        self.assertEqual(result, [])


    def test_threesum3(self):

        solution = Solution()
        nums = [-2,-1,0,3,1,2,4]

        result = solution.threesum(nums)
        self.assertEqual(result, [[-2,0,2],[-2,-1,3],[-1,0,1]])

if __name__ == '__main__':
    unittest.main()