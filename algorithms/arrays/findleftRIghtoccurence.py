class Solution:
    def searchRange(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        """
        left = self.binarySearch(nums,target,True)
        right = self.binarySearch(nums,target,False)
        return [left,right]

    def binarySearch(self,nums,target,leftbias):
        l,r = 0, len(nums)-1
        i = -1
        while l <=r:
            m = (l+r)//2
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                i=m
                if leftbias:
                    r = m-1
                else:
                    l=m+1
        return i