from collections import defaultdict

class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        places = ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
        n = len(score)
        a = [" "]*n
        d = defaultdict(int)

        for i in range(n):
            d[score[i]] = i
        score.sort(reverse=True)

        for i in range(n):
            if i < 3:
                a[d[score[i]]] = places[i]
            else:
                a[d[score[i]]] = str(i+1)
        return a
