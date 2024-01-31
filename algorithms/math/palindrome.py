class Solution:
    def palindrome(self, num):
        """
        :type num: int
        :rtype : bool
        """
        rev = 0
        if num < 0:
            x = str(num)
            rev = x[::-1]
        while num != 0:
            x = num%10
            rev = rev *10 + x
            x/=10
        return rev == num