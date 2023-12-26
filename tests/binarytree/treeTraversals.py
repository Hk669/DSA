import unittest
from algorithms.binarytree.treeTraversals import TreeNode, Solution

        # Example tree:     1
        #                  / \
        #                 2   3
        #                / \
        #               4   5


class TestTreeTraversals(unittest.TestCase):
    def test_inorderTraversal(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        solution = Solution()

        result = solution.inorderTraversal(root)
        expected = [4,2,5,1,3]

        self.assertEqual(result,expected)


    def test_preorderTraversal(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        solution = Solution()

        result = solution.preorderTraversal(root)
        expected = [1,2,4,5,3]

        self.assertEqual(result,expected)


    def test_postorderTraversal(self):

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)

        solution = Solution()

        result = solution.postOrderTraversal(root)
        expected = [4,5,2,3,1]

        self.assertEqual(result,expected)


if __name__ == '__main__':
    unittest.main()