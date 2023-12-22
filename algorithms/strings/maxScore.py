class Solution:
    def maxScore(self,s):
        """
        :type s: str
        :rtype : int
        """
        if s and len(s)>1:
            max_score = 0

            for i in range(1, len(s)):

                left = s[:i]
                right = s[i:]

                score = left.count('0') + right.count('1')
                max_score = max(score, max_score)

            return max_score
        
        return max(s.count('0'),s.count('1')) 
    