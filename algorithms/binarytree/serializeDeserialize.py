class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left , self.right = None, None

class Solution:
    def serialize(self,root):
        """
        :type root: TreeNode
        :rtype : str
        """

        res = []
        def dfs(root):
            if root is None:
                res.append('null')
                return 

            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        return ",".join(res)
    
    def deserialize(self, data):
        """
        :type data: str
        :rtype : TreeNode
        """

        vals = data.split(',')
        self.i = 0

        def dfs():
            if vals[self.i] == 'null':
                self.i +=1
                return None
            
            root = TreeNode(int(vals[self.i]))
            self.i +=1
            root.left = dfs()
            root.right = dfs()

            return root
        return dfs()

