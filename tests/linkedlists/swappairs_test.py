from algorithms.linkedlists.swapNodesInPairs import LinkedList, Solution
import unittest

class TestSwapInPairs(unittest.TestCase):

    def test_swapInPairs1(self):

        self.list = LinkedList(1)
        self.list.append(2)
        self.list.append(3)
        self.list.append(4)
        self.list.append(5)
        self.list.append(6)

        solution = Solution()

        res = solution.swapPairs(self.list)
        self.assertEqual(res, [2,1,4,3,6,5])

    def test_swapPairs2(self):
        
        self.list = LinkedList(3)
        self.list.append(2)
        self.list.append(4)
        self.list.append(5)

        solution = Solution()

        res = solution.swapPairs(self.list)
        self.assertEqual(res, [2,3,5,4])
    
if __name__ == '__main__':
    unittest.main()
