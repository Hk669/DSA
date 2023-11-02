class Solution:
    def twosum(self, nums, target):
        # the approach will be using hash map to reduce the time complexity 
        # in brute force method we used 2 for loops so the time complexity is O(n^2)
        # in this approach time comp is O(n)
        numIndex = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in numIndex:
                return [numIndex[complement], i] 
            numIndex[nums[i]] = i
        return []
    

    #Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
    # Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        numIndex = {} # hashmap to store in key value pair

        for i in range(len(numbers)):
            complement = target - numbers[i]

            if complement in numIndex:
                return [numIndex[complement]+1, i+1]  # the indices are starting from 1 so +1
            numIndex[numbers[i]] = i
        return []