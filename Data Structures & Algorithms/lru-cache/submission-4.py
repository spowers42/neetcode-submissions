class Node:
    def __init__(self, name, value, left=None, right=None):
        self.name = name
        self.value = value
        self.left = left
        self.right = right


class LRUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._key_to_node = {}
        self._head = Node("dummy node", "dummy")
        self._tail = self._head
        self._list_length = 0

    def get(self, key: int) -> int:
        if key not in self._key_to_node:
            return -1
        self._update_usage(key, None)
        return self._key_to_node[key].value

    def put(self, key: int, value: int) -> None:
        self._update_usage(key, value)

    def _update_usage(self, key, value):
        if node := self._key_to_node.get(key):
            if value is not None:
                node.value = value
            
            # just have to move to the tail, length isn't changing
            if node == self._tail:
                # do nothing
                return
            
            # we need to move to the tail
            if node.right:
                node.right.left = node.left
            node.left.right = node.right
            

            node.left = self._tail
            node.right = None

            self._tail.right = node
            self._tail = node
        else:
            # add a new node to the tail, and update head if needed
            node = Node(key, value, self._tail, None)
            self._tail.right = node
            self._tail = node
            self._key_to_node[key] = node
            self._list_length += 1

            if self._list_length > self._capacity:
                to_remove = self._head.right
                self._head.right = to_remove.right
                if to_remove.right:
                    to_remove.right.left = self._head
                else:
                    self._tail = self._head

                del self._key_to_node[to_remove.name]
                self._list_length -= 1
