from algorithms.linkedlists.mergeTwoSortedLists import Solution, LinkedList
import unittest

class TestLinkedList(unittest.TestCase):

    def test_mergesortedlists(self):

        self.l1 = LinkedList()
        self.l2 = LinkedList()

        self.l1.append(1)
        self.l1.append(2)
        self.l1.append(3)
        self.l1.append(4)
        self.l1.append(6)

        self.l2.append(5)
        self.l2.append(7)
        self.l2.append(8)
        self.l2.append(9)

        solution = Solution()
        mergelist = solution.mergeTwoLists(self.l1, self.l2)

        self.assertEqual(mergelist.display(), [1,2,3,4,5,6,7,8,9])



if __name__ == '__main__':
    unittest.main()
