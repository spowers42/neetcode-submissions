class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.dummy_head = ListNode(0)
        self.tail = self.dummy_head

    def get(self, index: int) -> int:
        current = self.dummy_head
        i = 0
        while i <= index:
            if current.next is None:
                return -1
            current = current.next
            i += 1
        return current.value

    def insertHead(self, val: int) -> None:
        node = ListNode(val, self.dummy_head.next)
        if self.dummy_head == self.tail:
            self.tail = node
        self.dummy_head.next = node

    def insertTail(self, val: int) -> None:
        node = ListNode(val)
        self.tail.next = node
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        current = self.dummy_head
        while i < index and current:
            current = current.next
            i += 1

        if current and current.next:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        current = self.dummy_head
        values = []
        while current.next:
            current = current.next
            values.append(current.value)
        return values
