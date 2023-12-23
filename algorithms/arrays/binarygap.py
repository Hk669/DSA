"""
the approach:
-- convert the given num to binary using the helper function
--- iterate through each digit and check if it is 1 
---- and check if the ingap is True then modify the maxGap and make the curr_gap = 0 because we reached ano0ther 1
--- else make the ingap as True cuz we entered the gap 
-- increase the curr_gap by 1 until we reach other 1
-- return the max_gap 
"""

class Solution:
    def binGap(self,num):
        """
        :type num: int
        :rtype : int
        """

        bin_num = self.helper(num)
        max_gap = 0
        curr_gap = 0
        ingap = False

        for dig in bin_num:
            if dig == '1':
                if ingap:
                    max_gap = max(max_gap, curr_gap)
                    curr_gap = 0
                else:
                    ingap = True
            else:
                curr_gap +=1
        return max_gap

    # used for converting the int to binary
    def helper(self,num):

            bin_num = ""
            while num > 0:

                dec = num%2
                bin_num = str(dec) + bin_num
                num = num//2

            return bin_num

