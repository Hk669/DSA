import unittest
from algorithms.binarytree.maxDepth import TreeNode,Solution

class MaxDepthTest(unittest.TestCase):

    def test_maxdepth1(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        
        solution = Solution()

        expected_depth = 3
        result = solution.maxDepth(root)
        self.assertEqual(result, expected_depth)

    def test_maxdepth2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        solution = Solution()

        expected_depth = 2
        result = solution.maxDepth(root)
        self.assertEqual(result, expected_depth)


if __name__ == '__main__':
    unittest.main()