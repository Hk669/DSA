def quick_sort(arr):

    """
    we'll assume the last element of the array as the partition element,
    using a for loop we will iterate through all
    the elements in the array and check whether its greater or lower,
    if greater -> append to left
    if lower -> append to right
    and use recursion to sort the left and right arrays
    """

    if len(arr)<=1:
        return arr

    partition = arr[-1]
    left = []
    right = []
    equal = []

    for i in arr:
        if i < partition:
            left.append(i)

        elif i > partition:
            right.append(i)

        else:
            equal.append(i)
    
    return quick_sort(left) + equal + quick_sort(right)
