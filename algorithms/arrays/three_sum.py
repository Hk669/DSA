class Solution:
    def threesum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = []
        nums.sort() # sorting the list given

        for i, a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue # skips the duplicate elements
            l,r = i+1, len(nums)-1
            while l<r:
                threesum = a + nums[l] + nums[r]

                if threesum<0:
                    l+=1 # if sum is less than target
                elif threesum>0:
                    r-=1 # if sum is greater than target
                else:
                    result.append([a,nums[l], nums[r]])
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1 # skips the duplicates
        return result

#refer arrays/helperimgs/3sum.png