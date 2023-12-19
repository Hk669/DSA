class Solution:
    def validAnagram(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype : bool
        """

        if len(s1) == len(s2):

            def helper(str):
                char_count = {}

                for s in str:
                    if s in char_count:
                        char_count[s] +=1
                    else:
                        char_count[s] = 1
                return char_count
            
            return helper(s1) == helper(s2)
        return False
    
# s1 = "tea"
# s2 = "ate"

# sol = Solution()
# print(sol.validAnagram(s1,s2))