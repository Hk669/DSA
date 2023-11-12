from algorithms.linkedlists.reversLinkedList import Solution, LinkedList
import unittest

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_append(self):
        self.linked_list.append(1)
        self.linked_list.append(4)
        self.linked_list.append(5)
        self.linked_list.append(6)
        self.linked_list.append(9)

        self.asserEqual(self.linked_list.display(), [1,4,5,6,9])

    def test_reverseList1(self):
        self.linked_list.append(1)
        self.linked_list.append(4)
        self.linked_list.append(5)
        self.linked_list.append(7)
        self.linked_list.append(3)
        self.linked_list.append(8)

        solution = Solution()
        reverse_list = solution.reverseLinkedList(self.linked_list)

        self.assertEqual(reverse_list.display(),[8,3,7,5,4,1])


    def test_reverseList2(self):
        self.linkedlist.append(2)
        self.linkedlist.append(4)
        self.linkedlist.append(6)
        self.linkedlist.append(7)
        self.linkedlist.append(8)
        self.linkedlist.append(1)

        solution = Solution()
        reversed_list = solution.reverseLinkedList(self.linkedlist)

        self.assertEqual(reversed_list.display(), [1,8,7,6,4,2])


if __name__ == '__main__':
    unittest.main()