class Solution:
    def reverseString(self,s):
        """
        :type s: str
        :rtype : str
        """

        if s:
            string = s.split()
            start , end = 0, len(string)-1

            while start < end:
                string[start] , string[end] = string[end], string[start]

                start+=1
                end-=1
            string = " ".join(string)
            return string
        
# s = "nice pne"
# sol = Solution()
# print(sol.reverseString(s))