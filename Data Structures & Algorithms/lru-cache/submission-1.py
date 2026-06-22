class Node:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}
        self.head, self.tail = Node(), Node()  # dummy nodes
        self.head.next, self.tail.prev = self.tail, self.head

    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def _insert(self, node):  # insert before tail
        node.prev, node.next = self.tail.prev, self.tail
        self.tail.prev.next = self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self._remove(self.map[key])
        self._insert(self.map[key])
        return self.map[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._remove(self.map[key])
        self.map[key] = Node(key, value)
        self._insert(self.map[key])
        if len(self.map) > self.cap:
            lru = self.head.next
            self._remove(lru)
            del self.map[lru.key]