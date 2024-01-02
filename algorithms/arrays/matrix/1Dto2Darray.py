from collections import defaultdict

class Solution:
    def twoDimArray(self,nums):
        """
        :type nums: List[int]
        :rtype : List[List[int]]
        """
        cnt = defaultdict(int)
        res = []

        for i in nums:
            row = cnt[i]
            if len(res) == row:
                res[row].append([])

            res[row].append(i)
            cnt[i] +=1

        return res
    
"""
we are tracking the frequency of the numbers, so at each
"""