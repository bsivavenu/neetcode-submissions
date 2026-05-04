class MyHashMap:

    def __init__(self):
        # Using a prime number to reduce collision probability
        self.size = 1009
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        
        # Check if key already exists to update it
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = [key, value]
                return
        
        # If key doesn't exist, append new pair
        bucket.append([key, value])

    def get(self, key: int) -> int:
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        hash_key = self._hash(key)
        bucket = self.table[hash_key]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)