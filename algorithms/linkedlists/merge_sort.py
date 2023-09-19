from linked_list import LinkedList


def merge_sort(linked_list):
    """
    
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right)

def split(linked_list):
    """
    Divide the unsorted list into sublists
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half,right_half 
    else:
        size = linked_list.size()
        mid = size//2

        #incomplete