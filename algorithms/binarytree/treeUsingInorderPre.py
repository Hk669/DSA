class Tree:
    def __init__ (self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right=right

class Solution:
    def buildTree(self,preorder,inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        if not preorder or not inorder:
            return None
        
        root = Tree(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid]) #returns the left subtree
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:]) #returns the right subtree

        return root
