def twoSum(arr,target):
    """
    :type arr: List[int]
    :type target: int
    :type rtype: List[int,int]
    :time-complexity O(n^2)
    """
    for i in range(len(arr)-1):
        for j in range(len(arr)):
            if i!=j and arr[i] +arr[j] == target:
                return [i,j]
