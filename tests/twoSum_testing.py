import unittest
from algorithms.arrays import (
    twoSum
)

class TwoSumTesting(unittest.TestCase):

    def testingTwosum(self):
        self.assertTrue(twoSum([23,45,10,12,34],22),[2,3])

        self.assertTrue(twoSum([1,2,3,4,5,6,7,8,9,10],3),[0,1])

        nums = [2,3,4,5,6]
        target = 11
        self.assertTrue(twoSum(nums,target),[3,4])

if __name__ == '__main__':
    unittest.main()
