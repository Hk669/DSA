class Solution:
    def rotateFunction(self,nums):
        """
        :type nums: List[int]
        :rtype : int
        """

        s = sum(nums)
        d = sum(idx*elem for idx, elem in enumerate(nums))
        max_val = d

        for pivot in range(len(nums)-1,-1,-1):
            d+= s - len(nums)*nums[pivot]
            max_val = max(d,max_val)

        return max_val