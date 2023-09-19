def merge_sort(arr):
    """
    we use divide and conquer method to sort the array,
    we use .extend method to append the left over elements in the 
    left and also right.
    """
    
    if len(arr)<=1:
        return arr
    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    #Recursion
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)

def merge(left,right):

    left_index,right_index = 0,0
    merged = []

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index+=1
        else:
            merged.append(right[right_index])
            right_index+=1
        
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged



