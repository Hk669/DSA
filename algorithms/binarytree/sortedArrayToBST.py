class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right, self.left = None, None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype : TreeNode
        """

        if not nums:
            return None
        
        l,r = 0, len(nums)-1
        m = (l+r)//2

        root = TreeNode(nums[m])
        root.left = self.sortedArrayToBST(nums[:m])
        root.right = self.sortedArrayToBST(nums[m+1:])

        return root