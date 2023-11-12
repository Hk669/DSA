from algorithms.linkedlists.middleofLinkedlist import LinkedList, Solution
import unittest


class TestMiddle(unittest.TestCase):

    def test_middleOfLinkedLists(self):
        
        self.list = LinkedList()
        self.list.append(3)
        self.list.append(5)
        self.list.append(6)
        self.list.append(7)
        self.list.append(9)
        self.list.append(1)
        self.list.append(11)


        solution = Solution()
        middle = solution.middleNode(self.list)

        self.assertEqual(middle.display(), [7])

    def test_middleOfLinkedList2(self):
        
        self.list = LinkedList()
        self.list.append(1)
        self.list.append(3)
        self.list.append(9)
        self.list.append(5)
        self.list.append(6)
        self.list.append(4)
        self.list.append(7)
        self.list.append(2)
        self.list.append(13)


        solution = Solution()
        middle = solution.middleNode(self.list)
        
        self.assertEqual(middle.display(),[6])


if __name__ == '__main__':
    unittest.main()
