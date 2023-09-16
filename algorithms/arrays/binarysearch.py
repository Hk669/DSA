"""
    Given array of integers: we have to find the element in the array
    we part the array into 2 
    if target greater than middle then we do the same thing to the right list
    if target is less than middle then we consider the left list
"""

# Without Recursion
class Solution(object):
    def binarysearch(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        
        while left <=right:
            mid = (left + right)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid+1
            else:
                right = mid-1

        return -1


#Using Recursion
def binarySearch(arr,target,left,right):

    mid = (left + right)//2
    target_idx = []

    if target == arr[mid]:
        target_idx.append(mid)
        return target_idx
    
    elif target > arr[mid]:
        binarySearch(arr,target, mid+1,right)
        
    else:
        binarySearch(arr,target,left,mid-1)
