# Implementation of Open Addressing (Linear Probing) in Python
"""
Time Complexity:
1) On average case, time complexity will be O(1).
2) On worst case, time complexity will be O(n) because of the cluster formed.

Space Complexity
The space complexity of the hash table is O(n)

"""
class MyHash:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [-1]*capacity
        self.size = 0

    def hash(self, key):
        return key % self.capacity
    
    def search(self, key):
        h = self.hash(key)
        start = h

        while self.table[h] != -1:
            if self.table[h] == key:
                return True 

            h = (h + 1) % self.capacity
            if h == start:
                return False
        return False

    def insert(self, key):
        if self.size == self.capacity:
            return False
        
        if self.search(key) == True:
            return False
        
        h = self.hash(key)

        while self.table[h] not in (-1, -2):
            h = (h+1) % self.capacity

        self.table[h] = key
        self.size += 1
        return True
    
    def remove(self, key):
        h = self.hash(key)
        start = h

        while self.table[h] != -1:
            if self.table[h] == key:
                self.table[h] = -2
                return True
            h = (h + 1) % self.capacity
            if h == start:
                return False
        return False
    
h = MyHash(7)
h.insert(70)
h.insert(71)
h.insert(9)
h.insert(56)
h.insert(72)

print(h.table)

print(h.search(56))
h.remove(56)
print(h.search(56))
h.remove(56)

print(h.table)
