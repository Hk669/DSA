class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


# def SameTree(p,q):

#     if not p and not q:
#         return True

#     if not p or not q:
#         return False
    
#     if p.val == q.val and SameTree(p.left, q.left) and SameTree(p.right, q.right)