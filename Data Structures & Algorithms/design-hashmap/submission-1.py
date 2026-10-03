class MyHashMap:

    def __init__(self):
        self.modulo = 10007
        self.store = [[] for _ in range(self.modulo)]

    def put(self, key: int, value: int) -> None:
        hesh = self.getHash(key)
        found = self.find(key)

        if(found == -1):
            self.store[hesh].append([key, value])
        else:
            self.store[hesh][found][1] = value

    def get(self, key: int) -> int:
        hesh = self.getHash(key)
        found = self.find(key)

        if(found == -1):
            return -1
        else:
            return self.store[hesh][found][1]

    def remove(self, key: int) -> None:
        hesh = self.getHash(key)
        found = self.find(key)

        if(found != -1):
            self.store[hesh].pop(found)
        
    
    def getHash(self, key: int) -> int:
        return key % self.modulo

    def find(self, key: int) -> int:
        hesh = self.getHash(key)
        part = self.store[hesh]
        for i, pair in enumerate(part):
            if(pair[0] == key):
                return i

        return -1



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)