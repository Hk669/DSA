class Solution:
    def bubblesort(self, arr):
        """
        :type arr: List[int]
        :rtype arr: List[int]
        """
        if len(arr) <= 0:
            return arr
        
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):

                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i] #swap elements
                
        return arr
