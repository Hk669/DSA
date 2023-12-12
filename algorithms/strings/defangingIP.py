class Solution:
    def defangIPaddress(self,address):
        """
        :type address : str
        :rtype : str
        """
        if len(address) > 0:
            res = address.replace('.','[.]')
            return res
        return address
    