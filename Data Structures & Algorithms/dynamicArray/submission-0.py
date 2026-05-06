class DynamicArray:
    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError("The array must be allocated with at least 1 element.")
        self._array = [0] * capacity
        self._capacity = capacity
        self._end = -1

    def get(self, i: int) -> int:
        if i >= self._capacity:
            raise ValueError("Index out of range")
        return self._array[i]

    def set(self, i: int, n: int) -> None:
        if i >= self._capacity:
            raise ValueError("Index out of range")
        self._array[i] = n

    def pushback(self, n: int) -> None:
        new_end = self._end + 1
        if new_end >= self._capacity:
            self.resize()
        self._array[new_end] = n
        self._end = new_end

    def popback(self) -> int:
        val = self._array[self._end]
        self._end -= 1
        return val

    def resize(self) -> None:
        new_capacity = self._capacity * 2
        new_array = [0] * new_capacity
        for idx in range(self.getSize()):
            new_array[idx] = self._array[idx]
        self._array = new_array
        self._capacity = new_capacity

    def getSize(self) -> int:
        return self._end + 1

    def getCapacity(self) -> int:
        return self._capacity
