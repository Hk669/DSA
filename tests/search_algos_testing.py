import unittest
from algorithms.arrays import (
    binarySearch
)

class SearchingAlgosTest(unittest.TestCase):
    def test_binarysearch(self):
        self.assertTrue(binarySearch([1,2,3,4,5,67,98,107],98),6)

        self.assertTrue(binarySearch([23,45,64,73,87,89,98],23),0)

        self.assertEqual(binarySearch([1, 2, 3, 4, 5], 6), -1)


if __name__ == '__main__':
    unittest.main()
