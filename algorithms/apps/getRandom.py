import random

class RandomizedSet:
    def __init__(self):
        self.randomset = set()

    def insert(self,val):
        """
        :type val: int
        :rtype : bool
        """
        if val not in self.randomset:
            self.randomset.add(val)
            return True
        return False
    
    def remove(self,val):
        """
        :type val: int
        :rtype : bool
        """
        if val in self.randomset:
            self.randomset.remove(val)
            return True
        return False
    
    def get_random(self):
        """
        :rtype : int
        """
        if len(self.randomset) >=1:
            return random.choice(list(self.randomset))
        