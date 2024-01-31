class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype : List[int]
        """
        n = len(temperatures)
        answer = [0]*n
        stack = []

        for i in range(n):
            j =i+1
            while j < n and temperatures[i] > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                answer[prev_idx] = i - prev_idx
            stack.append(i)
        return answer
