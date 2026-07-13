class HashEntry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * self.capacity

    def insert(self, key: int, value: int) -> None:
        location = self._hash(key)

        while True:
            if self.table[location] and self.table[location].key == key:
                self.table[location].value = value
                break
            elif self.table[location] is None:
                entry = HashEntry(key, value)
                self.table[location] = entry
                self.size += 1
                break
            location = (location + 1) % self.capacity

        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        location = self._hash(key)
        while self.table[location]:
            if self.table[location].key == key:
                return self.table[location].value
            location = (location + 1) % self.capacity
        return -1

    def remove(self, key: int) -> bool:
        location = self._hash(key)
        while self.table[location]:
            if self.table[location].key == key:
                self.table[location] = None
                self.size -= 1
                return True
            location = (location + 1) % self.capacity
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        new_table = [None] * self.capacity
        for element in self.table:
            if element:
                idx = self._hash(element.key)
                new_table[idx] = element
        self.table = new_table

    def _hash(self, value: int) -> int:
        return value % self.capacity
