class Solution:
    def signFun(self,arr):
        """
        :type arr: List[int]
        :rtyoe : int
        """

        prod = 1
        for i in range(len(arr)):
            prod *= arr[i]

        if prod > 0:
            return 1
        elif prod < 0:
            return -1
        else:
            return 0
