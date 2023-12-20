class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left= None
        self.right = None

class Solution:
    def preOrder(self,tree):
        """
        :type tree: TreeNode
        :rtype : List[int]
        """
        arr = []
        def helper(root):
            if root is None:
                return

            arr.append(root.val)
            left = helper(root.left)
            right = helper(root.right)

            return arr
        helper(tree)
        return arr
    

sol = Solution()
tree = TreeNode(2)
tree.left = TreeNode(3)
tree.left.right = TreeNode(4)
tree.left.left = TreeNode(5)
tree.right = TreeNode(6)
tree.right.left = TreeNode(7)


print(sol.preOrder(tree))