# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        if not inorder:
            return None

        root = TreeNode(postorder.pop())
        idx = inorder.index(root.val)

        root.left = self.buildTree(inorder[:idx], postorder)
        root.right = self.buildTree(inorder[idx+1:], postorder)

        return root
    