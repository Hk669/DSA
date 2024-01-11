class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left, self.right = None, None
        
class Solution:
    def maxAncestorDiff(self,root):
        """
        :type root: TreeNode
        :rtype :int
        """

        def helper(root,min_val,max_val):
            if root is None:
                return max_val - min_val
            
            min_val = min(min_val,root.val)
            max_val = max(max_val,root.val)
            
            left = helper(root.left,min_val,max_val)
            right = helper(root.right,min_val,max_val)

            return left-right
        
        return helper(root,root.val,root.val)
    