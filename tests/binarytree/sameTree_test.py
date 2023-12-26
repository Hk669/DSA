import unittest
from algorithms.binarytree.sameTree import TreeNode, Solution

class TestSameTree(unittest.TestCase):

    def test_sameTree(self):

        # tree1
        tree1 = TreeNode(1)
        tree1.right = TreeNode(2)
        tree1.left = TreeNode(2)

        # tree2 
        tree2 = TreeNode(1)
        tree2.right = TreeNode(2)
        tree2.left = TreeNode(2)

        solution = Solution()
        result = solution.isSameTree(tree1,tree2)

        self.assertTrue(result)
