class Tree:
    def __init__ (self, val=0, left=None, right=None):
        self.val = val
        self.left= left
        self.right = right

class Solution:
    def symmetricTree(self,root): 
        
        def dfs(left, right):

            #check if left and right subtree are null
            if not left and not right:
                return True
            # any of the left or right is null
            if not left or not right:
                return False
            
            return ( left.val == right.val and 
                    dfs(left.left, right.right) and
                    dfs(left.right, right.left)
                    )
        
        return dfs(root.left, root.right)
    
# refer helperimgs/symmetric.png