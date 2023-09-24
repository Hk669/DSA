class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    @staticmethod
    def inorderTraversal(tree):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(tree, array=[]):
            if tree is not None:
                helper(tree.left,array)
                array.append(tree.val)
                helper(tree.right,array)
            return array
        return helper(tree)
    
    @staticmethod
    def preorderTraversal(tree):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(tree,array=[]):
            if tree is not None:
                array.append(tree.val)
                helper(tree.left,array)
                helper(tree.right,array)

            return array
        return helper(tree)
    
    @staticmethod
    def postOrderTraversal(tree):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(tree,array=[]):

            if tree is not None:
                helper(tree.left,array)
                helper(tree.right,array)
                array.append(tree.val)
            return array
        
        return helper(tree)
        