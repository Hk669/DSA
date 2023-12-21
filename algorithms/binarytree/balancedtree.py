class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root):
            if root is None:
                return [True,0]

            left,right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and 
                    abs(left[1] - right[1]) <= 1)
            return [balanced, 1+ max(left[1],right[1])]

        return dfs(root)[0]

"""
by using the bottom-up approach and calculating the height
of the left and subtrees and recursively checking for the whole tree
if balanced returns True.

Balanced Tree: The height difference of left and right subtree 
                should be less than or equal to 1
"""
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left, self.right = None, None
class Solution:
    def balancedTree(self,root):

        def dfs(root):
            if root is None:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and
                        abs(left[1]- right[1])<=1)
            return [balanced, 1+ max(left[1], right[1])]

        return dfs(root)[0] # to return in bool