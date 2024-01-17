class MyHashMap(object):

    def __init__(self, capacity=16):
        self.capacity = capacity
        self.buckets = [None]*capacity
    
    def _hash(self,key):
        return hash(key)%self.capacity

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        index = self._hash(key)
        if self.buckets[index] is None:
            self.buckets[index] = []
        bucket = self.buckets[index]

        for i,(existing_key,_) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key,value)
                return 
        bucket.append((key,value))

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        index = self._hash(key)
        if self.buckets[index] is not None:
            for existing_key, value in self.buckets[index]:
                if existing_key == key:
                    return value
        return None

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = self._hash(key)

        if self.buckets[index] is not None:
            for i, (existing_key, _) in enumerate(self.buckets[index]):
                if existing_key == key:
                    del self.buckets[index][i]
                    return 

