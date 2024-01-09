class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def leafSimilar(self,root1,root2):
        """
        :type root1:TreeNode
        :type root2:TreeNode
        :rtype :bool
        """
        leaves1, leaves2 = [], []
        self.findLeaves(root1,leaves1)
        self.findLeaves(root2,leaves2)
        return leaves1 == leaves2
    
    def findLeaves(self,root,leaves):
        """
        :type root:TreeNode
        :type leaves:List[int]
        """
        if root is None:
            return
        if root.left is None and root.right is None:
            leaves.append(root.val)
        self.findLeaves(root.left,leaves)
        self.findLeaves(root.right,leaves)
        