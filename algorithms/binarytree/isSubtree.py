class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def isSubtree(self,root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        """

        if root is None:
            return False
        
        def helper(root, subroot):

            if not root and not subroot:
                return True
            
            if not root or not subroot:
                return False
            
            return (
                root.val == subroot.val
                and helper(root.left,subroot)
                and helper(root.right, subroot)
            )
        
        return helper(root,subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)