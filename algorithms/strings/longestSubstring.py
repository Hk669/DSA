class Solution:
    def lengthLongestSubsequence(self,s):
        """
        :type s: str
        :rtype : int
        """

        i = j = max_len = 0
        substring = set()

        while i < len(s) and j < len(s):
            if s[i] not in substring:
                substring.add(s[i])
                max_len = max(max_len, i-j+1)
                i+=1
            
            substring.remove(s[j])
            j+=1
        return max_len
    
"""
the approach is sliding window
where the i is incremented with iterations and if the substring is repeated then remove the substring from the set and 
increment the j till it removes all the elements in the set. then it reaches i = j point.
same process continues till i is out of len.
and then return the max of max_len of the substring we added into the set in each iteration
"""
