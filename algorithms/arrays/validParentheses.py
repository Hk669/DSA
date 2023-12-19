class Solution:
    def IsValid(self, s):
        """
        :type s: str
        :rtype : bool
        """

        stack = []
        mapParentheses = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for c in s:
            if c in mapParentheses:
                if stack and stack[-1] == mapParentheses[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack
