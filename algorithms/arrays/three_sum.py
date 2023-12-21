"""
approach:
firstly sort the list given, to use the 2 pointers to check the sum of 3 
the first index remains same, assign left, right as i+1 and len(nums)-1 respectively
now add them and check the conditions:
-- if the sum > 0 then move the right pointer to left (decrement by 1) 
-- if the sum < 0 then move the left pointer to right ( increment by 1)
-- else append the first index , left and right to the list
-- move the first index to next element in the sorted list

to avoid the duplicates check the condition if the left index is same as the before index (nums[l] == nums[l-1])
if yes then l+=1
"""

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
    

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype : List[List[int]]
    """

    res =[]
    nums.sort()

    for i, a in enumerate(nums):
        
        if i > 0 and a == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1

        while l < r:
            three_sum = a + nums[l] + nums[r]

            if three_sum > 0:
                r-=1
            elif three_sum< 0:
                l+=1
            else:
                res.append([a,nums[l],nums[r]])
                l+=1
                while l < r and nums[l] == nums[l-1]:
                    l+=1
    return res


nums = [-1,0,1,2,-1,-4,-1]
print(threeSum(nums))

