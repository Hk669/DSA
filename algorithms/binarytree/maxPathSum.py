class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def maxPathSum(self,root):
        """
        :type root: TreeNode
        :rtype : int
        """

        max_sum = [float('-inf')]

        # postorder approach
        def helper(root):
            if root is None:
                return 0

            left = max(helper(root.left),0)
            right = max(helper(root.right),0)
            max_sum[0] = max(max_sum[0], left+right+root.val)

            return max(left,right) +root.val
        helper(root)
        return max_sum[0]