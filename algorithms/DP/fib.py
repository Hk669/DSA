"""
this algo can be used for the number range (0 < n < 30), after that it takes so much time to return the fib.
"""
# class Solution:
#     def fib(self, n):
#         """
#         :type n: int
#         :rtype : int
#         """
#         memo = {} # to avoid repeated calculations for the high numbers

#         def helper(n):
#             if n in memo:
#                 return memo[n]
#             if 0<n<=2:
#                 res = 1
#                 return res
#             elif n == 0:
#                 res = 0
#                 return res
#             else:
#                 res = helper(n-1) + helper(n-2)
#                 return res
            
#             memo[n] = res
#         return helper(n)
    

"""
to reduce the time of calculating we use the iterative approach
"""
class Solution:
    def fib(self, n):
        if n <= 1:
            return n

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b

        return b


# n = 40
# sol = Solution()
# print(sol.fib(n))
    