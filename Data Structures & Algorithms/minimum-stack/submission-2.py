class MinStack:
    def __init__(self):
        self._stack = []
        self._smallest_stack = []  # length, smallest value up to that point

    def push(self, val: int) -> None:
        if len(self._stack)== 0:
            smallest_value = val
        else:
            smallest_value = val if val < self._smallest_stack[-1] else self._smallest_stack[-1]
        
        self._smallest_stack.append(smallest_value)
        self._stack.append(val)

    def pop(self) -> None:
        self._stack.pop()
        self._smallest_stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._smallest_stack[-1]
