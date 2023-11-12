from algorithms.linkedlists.mergeKsorted import Solution, LinkedList
import unittest

class TestKsorted(unittest.TestCase):

    def test_mergeKsorted(self):
        """
        :type lists : List[ListNode]
        """
        self.lists = []
        self.l1 = LinkedList()
        self.l2 = LinkedList()
        self.l3 = LinkedList()

        self.l1.append(1)
        self.l1.append(5)
        self.l1.append(7)
        self.l1.append(8)
        self.l1.append(10)

        self.l2.append(2)
        self.l2.append(4)
        self.l2.append(9)

        self.l3.append(3)
        self.l3.append(6)
        self.l3.append(11)
        self.l3.append(12)

        self.lists.append(self.l1)
        self.lists.append(self.l2)
        self.lists.append(self.l3)

        solution = Solution()
        ksortedlists = solution.mergeKLists(self.lists)

        self.assertEqual(ksortedlists.display(), [1,2,3,4,5,6,7,8,9,10,11,12])


if __name__ == '__main__':
    unittest.main()
