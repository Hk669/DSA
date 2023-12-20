"""
approach:
instead of rotating each element we can cut off some unnecessary steps by K = K % len(arr)
then reverse the whole arr
reverse the elements from 0 to K-1 ( as the elements start from 0 , k should be decremented by 1)
reverse the next elements of to the end
return the arr
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        k = k % len(nums) # to avoid unnecessary rotations

        self.reverse(nums,0,len(nums)-1) # reverse the whole array
        self.reverse(nums,0,k-1) # reverse the first k elements
        self.reverse(nums,k,len(nums)-1) # reverse the next elements of an array

        return nums
        
    # helper function to reverse an array
    def reverse(self,nums,start,end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start+=1
            end-=1
        return nums
        