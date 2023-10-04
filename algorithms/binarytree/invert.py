class TreeNode:
    def __init__(self,val=0,left=None, right =None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self,root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """       
        if root is None:
            return root
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        #swap the values
        root.left , root.right = root.right, root.left

        return root
    