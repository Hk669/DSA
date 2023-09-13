"""
    Given array of integers: we have to find the element in the array
    we part the array into 2 
    if target greater than middle then we do the same thing to the right list
    if target is less than middle then we consider the left list
"""

# Without Recursion
def binarySearchh(arr,target):

    left = 0
    right = len(arr)-1
    mid = (left+right)//2

    target_idx = []

    while left <=right:
        if arr[mid] == target:
            target_idx.append(mid)
            return target_idx
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid-1

    return target_idx


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
