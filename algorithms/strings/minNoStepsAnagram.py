from collections import defaultdict
class Solution:
    def minSteps(self,s,t):
        """
        :type s:str
        :type t:str
        :rtype :int
        """
        fs = self.frequency(s)
        ft = self.frequency(t)

        if fs == ft:
            return 0
        diff = 0
        for c,cnt_s in fs.items():
            if c in ft:
                if cnt_s == ft[c]:
                    diff+=cnt_s
                else:
                    diff += min(cnt_s,ft[c])
        return len(s) - diff
    
    def frequency(self,s):
        """
        :type s:str
        :rtype :dict
        """
        hashmap = defaultdict(int)
        for c in s:
            hashmap[c] +=1
        return hashmap
    