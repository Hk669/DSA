class Solution:
    def permutation(self,nums):
        """
        :type nums: List[int]
        :rtype : List[List[int]]
        """

        if len(nums) == 1:
            return [nums]
        
        res = []
        for i,num in enumerate(nums):
            rest = nums[:i] + nums[i+1:]
            per_rest = self.permutation(rest)
            res.extend([num] + perm for perm in per_rest)

        return res


"""
we use the recursion to solve the permutations problem, where we need to find the sets of arrangement
of the given elements in different order.
"""