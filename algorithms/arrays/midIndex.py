class Solution:
    def findMidIndex(self,nums):
        """
        :type nums List[int]
        :rtype : int
        """
    
        total_sum = sum(nums)
        curr_sum=0 #leftSum

        for i,num in enumerate(nums):
            total_sum -= num # this will be the rightSum

            if total_sum == curr_sum:
                return i
            curr_sum+=num

        return -1
    
# find pivot index (724)