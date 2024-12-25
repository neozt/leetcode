from collections import deque

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'Node({self.key}, {self.value})'

    def print(self):
        current = self
        output = []
        while current:
            output.append(repr(current))
            current = current.next

        print(" ".join(output))

class LRUCache:



    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}
        self.head.print()

    def deleteNode(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        node.next = node.prev = None

    def addToFront(self, node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        temp.prev = node
        node.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        prev_node = self.map[key]
        del self.map[prev_node.key]
        self.deleteNode(prev_node)
        self.addToFront(prev_node)
        self.map[key] = prev_node

        return prev_node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            prev_node = self.map[key]
            self.deleteNode(prev_node)
            new_node = Node(key, value)
            self.addToFront(new_node)
            self.map[key] = new_node
        else:
            if len(self.map) == self.capacity:
                last_node = self.tail.prev
                del self.map[last_node.key]
                self.deleteNode(self.tail.prev)
            node = Node(key, value)
            self.addToFront(node)
            self.map[key] = node



["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
val = cache.get(1)
print(val)
cache.put(3, 3)
val = cache.get(2)
print(val)
cache.put(4, 4)
val = cache.get(1)
print(val)

val = cache.get(3)
print(val)

val = cache.get(4)
print(val)
