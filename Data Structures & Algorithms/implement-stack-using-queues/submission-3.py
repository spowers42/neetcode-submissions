class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
        self.size = 0

    def push(self, value):
        node = Node(value)
        self.tail.next = node
        self.tail = self.tail.next
        self.size += 1

    def peak(self):
        if self.size > 0:
            return self.head.next.value
        return None

    def pop(self):
        if self.size > 0:
            target = self.head.next
            self.head.next = target.next
            if self.size == 1:
                self.tail = self.head
            self.size -= 1
            return target.value
        return None

    def empty(self):
        return self.size == 0


class MyStack:
    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        self.queue.push(x)

    def pop(self) -> int:
        for i in range(self.queue.size - 1):
            self.queue.push(self.queue.pop())
        return self.queue.pop()

    def top(self) -> int:
        for i in range(self.queue.size):
            if i == self.queue.size - 1:
                value = self.queue.peak()
            self.queue.push(self.queue.pop())

        return value

    def empty(self) -> bool:
        return self.queue.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
