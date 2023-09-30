class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        
        def dfs(root):
            if root is None:
                return 0
            
            left, right = dfs(root.left), dfs(root.right)
            self.diameter =max(self.diameter, left+ right)

            return 1+ max(left,right)
        
        dfs(root)
        return self.diameter
        