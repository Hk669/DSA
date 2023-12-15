#66
class Solution:
    def plusOne(self,digits):
        """
        :type digits: List[int]
        :rtype : List[int]
        """

        if digits:
            digits[-1] +=1
            for i in range(len(digits)-1, 0, -1):
                if digits[i] == 10:
                    digits[i] = 0
                    digits[i-1] +=1
            if digits[0] == 10:
                digits[0] = 1
                digits.append(0)

            return digits