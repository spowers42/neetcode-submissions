class Node:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        if self.head:
            return False
        return True

    def append(self, value: int) -> None:
        node = Node(value)
        if not self.tail:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = self.tail.next

    def appendleft(self, value: int) -> None:
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head
            self.head.previous = node
            self.head = node

    def pop(self) -> int:
        value = -1
        if self.head:
            value = self.tail.value
            self.tail = self.tail.previous
            if self.tail:
                self.tail.next = None
            else:
                self.head = self.tail
        return value

    def popleft(self) -> int:
        value = -1
        if self.head:
            value = self.head.value
            self.head = self.head.next
            if self.head:
                self.head.previous = None
            else:
                self.tail = self.head
        return value
