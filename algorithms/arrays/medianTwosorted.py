class Solution:
    def medianTwoSorted(self,nums1,nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype : float
        """
        s = len(nums1) + len(nums2)
        half = s//2

        med1 , med2 = None, None
        i=j=0
        while i+j < half +1:
            if i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    med1 = med2
                    med2 = nums1[i]
                    i+=1
                elif nums1[i] > nums2[j]:
                    med1 = med2
                    med2 = nums2[j]
                    j+=1
                
            elif i < len(nums1):
                med1 = med2
                med2 = nums1[i]
                i+=1
            else:
                med1 = med2
                med2 = nums2[j]
                j+=1

        if s%2==1:
            return med2
        else:
            return (med1+med2)/2.0
        