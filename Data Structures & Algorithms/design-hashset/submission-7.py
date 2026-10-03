class MyHashSet:

    def __init__(self):
        self.modulo = 10007
        self.store = [[] for _ in range(self.modulo)]

    def add(self, key: int) -> None:
        hesh = self.getHash(key)
        if(not self.contains(key)):
            self.store[hesh].append(key)

    def remove(self, key: int) -> None:
        hesh = self.getHash(key)
        if(self.contains(key)):
            self.store[hesh].remove(key)

    def contains(self, key: int) -> bool:
        hesh = self.getHash(key)
        return key in self.store[hesh]

    def getHash(self, key: int) -> int:
        return key % self.modulo



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)