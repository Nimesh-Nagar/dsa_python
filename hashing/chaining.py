
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

h.insert(70)
h.insert(71)
h.insert(9)
h.insert(56)
h.insert(72)

print(h.search(56))
h.remove(56)
print(h.search(56))

h.remove(56)





