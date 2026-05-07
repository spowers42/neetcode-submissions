class MinStack:
    def __init__(self):
        self._stack = []
        self._smallest_map = {}  # length, smallest value up to that point

    def push(self, val: int) -> None:
        l = len(self._stack)
        if l == 0:
            smallest_value = val
        else:
            smallest_value = val if val < self._smallest_map[l] else self._smallest_map[l]
        self._smallest_map[l + 1] = smallest_value

        self._stack.append(val)

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._smallest_map[len(self._stack)]
