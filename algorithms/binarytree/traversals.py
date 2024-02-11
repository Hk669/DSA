# Definition for a binary tree node.
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def treeLevelOrder(self,root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return root
        
        res = []
        q = deque([root])

        while q:
            qLen = len(q)
            level = []

            for i in range(qLen):
                node = q.popleft()

                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if level:
                res.append(level)
        return res
