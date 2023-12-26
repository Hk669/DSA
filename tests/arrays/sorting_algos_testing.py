import unittest
from algorithms.sorting import merge_sort, quick_sort


def is_sorted(array):
    """
    Helper function to check if the given array is sorted or not
    returns false if the array is not sorted in ascending order
    """
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            return False

    return True


class TestSortingAlgos(unittest.TestCase):

    def test_quicksort(self):
        self.assertTrue(is_sorted(quick_sort([1,5,64,2,7,3,
                                              67,4,47])))
        
        self.assertTrue(is_sorted(quick_sort([3,56,24,235,2,35,7,1,9,
                                              10,14,13])))
        
    def test_merge_sort(self):
        self.assertTrue(is_sorted(merge_sort([3,56,24,235,2,35,7,1,9,
                                              10,14,13])))
        
        self.assertTrue(is_sorted(quick_sort([1,5,64,2,7,3,
                                              67,4,47])))
        

if __name__ == "__main__":
    unittest.main()
    