class Solution:
    def myAtoi(self, s):
        """
        :type s: str
        :rtype : int
        """
        if s:
            num = "".join(s.split())
            res = 0
            sign = 1

            for n in num:
                if n in '+-':
                    sign = -1 if n == '-' else 1
                elif n.isdigit():
                    res = res*10 + int(n)
                else:
                    break

            res*= sign
            return res
