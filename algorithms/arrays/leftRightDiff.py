class Solution:
    def leftRightDifference(self,nums):
        """
        :type nums: List[int]
        :rtype : list[int]
        time complexity : O(n) + O(n)
        """

        leftSum = [0]
        rightSum = [0]
        res = []

        # from index 0 to last but 1 element , cuz we dont need last element
        for num in nums[:-1]:
            leftSum.append(leftSum[-1]+num)
        
        # reverse the nums to get the sum from right side
        for num in nums[::-1][:-1]:
            rightSum.append(rightSum[-1]+num)

        #reverse the rightSum
        rightSum = rightSum[::-1]

        #for the abs difference
        for i in range(len(leftSum)):
            res.append(abs(leftSum[i])-abs(rightSum[i]))

        return [abs(val) for val in res]
    

    def leftRightDiff(self,nums):
        """
        :type nums: List[int]
        :rtype : List[int]
        time complexity : O(n)
        """

        res = []
        sum_el = sum(nums)

        for i, num in enumerate(nums):
            if i ==0:
                res.append(sum_el-nums[0])

            else:
                res.append(res[i-1]+num+nums[i-1])

        return [abs(val) for val in res]
    