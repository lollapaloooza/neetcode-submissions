class MyHashSet:

    def __init__(self):
        self.modulo = 10007
        self.store = [[] for _ in range(self.modulo)]

    def add(self, key: int) -> None:
        hashKey = self.getHash(key)
        if(not self.contains(key)):
            self.store[hashKey].append(key)

    def remove(self, key: int) -> None:
        hashKey = self.getHash(key)
        if(self.contains(key)):
            self.store[hashKey].remove(key)

    def contains(self, key: int) -> bool:
        hashKey = self.getHash(key)
        return key in self.store[hashKey]
    
    def getHash(self, key: int) -> int:
        return key % self.modulo


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)