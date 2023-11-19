from algorithms.linkedlists.palindromeLinkedList import ListNode, LinkedList, Solution
import unittest

class TestPalindromeList(unittest.TestCase):

    def test_palindromeList1(self):

        self.list = LinkedList(2)
        self.list.append(3)
        self.list.append(4)
        self.list.append(7)
        self.list.append(4)
        self.list.append(3)
        self.list.append(2)

        solution = Solution()

        res = solution.palindromeLinkedList(self.list)

        self.assertEqual(res, True)

    def test_palindromeList2(self):

        self.list = LinkedList(1)
        self.list.append(3)
        self.list.append(5)
        self.list.append(9)
        self.list.append(1)

        solution = Solution()

        res = solution.palindromeLinkedList(self.list)

        self.assertEqual(res, False)

if __name__ == '__main__':
    unittest.main()