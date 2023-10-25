class Tree:
    def __init__ (self, val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def depthFirstSearch(self, tree):
        if tree is not None:
            result = [tree.val]
            if tree.left:
                result.extend(self.depthFirstSearch(tree.left))
            if tree.right:
                result.extend(self.depthFirstSearch(tree.right))
            return result
        return []

tree = Tree(2)
tree.left = Tree(3)
tree.left.left = Tree(5)
tree.right = Tree(7)
tree.right.left = Tree(9)
tree.right.right = Tree(6)

result = Solution()
dfs = result.depthFirstSearch(tree)
print(dfs)