import unittest
from algorithms.binarytree.maxAncestorDiff import TreeNode,Solution

class TestAncestorDiff(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_maxAncestorDiff(self):

        self.root = TreeNode(8)
        self.root.left = TreeNode(3)
        self.root.left.left = TreeNode(1)
        self.root.right = TreeNode(10)
        self.root.right.right = TreeNode(14)
        self.root.right.right.left = TreeNode(14)
        self.root.left.right = TreeNode(6)
        self.root.left.right.left = TreeNode(4)
        self.root.left.right.right = TreeNode(7)

        result = 7
        sol = self.solution.maxAncestorDiff(self.root)
        self.assertEqual(result,sol)


    def test_maxAncestorDiff2(self):

        self.root = TreeNode(1)
        self.root.right = TreeNode(2)
        self.root.right.right = TreeNode(0)
        self.root.right.right.left = TreeNode(3)

        sol = self.solution.maxAncestorDiff(self.root)
        result = 3
        self.assertEqual(result,sol)


if __name__ == '__main__':
    unittest.main()
