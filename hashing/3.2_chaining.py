# Implementation of Chaining
"""
Space Complexity:
O(n + b) 
where
    n is the number of elements inserted
    b is the number of buckets in the hash table

Time Complexity: 
In the worst-case scenario, all elements might be in the same bucket, 
leading to O(n) time where 'n' is the total number of elements in the hash table.
"""

class MyHash():
    def __init__(self, size):
        self.BUCKET = size
        self.table = [[] for _ in range(size)]
        
    def insert(self, value):
        idx = value % self.BUCKET
        self.table[idx].append(value)
        
    def remove(self, value):
        idx = value % self.BUCKET
        if value in self.table[idx]:
            self.table[idx].remove(value)
    
    def search(self, value):
        idx = value % self.BUCKET
        return value in self.table[idx]
    

h = MyHash(7)

print(h.table)
h.insert(70)
h.insert(71)
h.insert(9)
h.insert(56)
h.insert(72)
print(h.table)

print("Searching 56 ",h.search(56)) # True
print("Removing 56 ")
h.remove(56)

print("Searching 56 after deleting ",h.search(56)) # False

h.remove(56)





