# chaining  

class HashTable:

    def __init__(self, size):
        self.MAX = size
        self.arr = [ [] for _ in range(self.MAX)]

    def get_hash(self, key):
        hash = 0 
        for char in key:
            hash += ord(char)
        
        return hash % self.MAX 
    
    def insert(self, key, value):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break

        if not found:
            self.arr[h].append((key, value))

    def search(self, key):
        h = self.get_hash(key)

        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        return None
    
    def delete(self, key):
        h = self.get_hash(key)

        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
                return True
        return False
    

ht = HashTable(7)
print(ht.arr)

print(ht.get_hash('march 17'))

ht.insert('march 6', 130)
ht.insert('march 17', 170)
ht.insert('march 6', 220)
ht.insert('march 1', 22)


print(ht.arr)

print(ht.search('march 6'))




