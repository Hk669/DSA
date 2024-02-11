from collections import deque

class Tree:
    def __init__ (self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):

        result = []
        q = deque([root] if root else [])

        while q:
            qlen = len(q)
            level = []

            for i in range(qlen):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level = reversed(level) if len(result) % 2 else level
            result.append(level)
        return result
    
# checkout helperimgs/103.png for the explanation