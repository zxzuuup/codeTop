class DLinkedList:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.cache = dict()
        self.head = DLinkedList()
        self.tail = DLinkedList()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int):
        if key not in self.cache.keys():
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.val

    def put(self, key: int, value: int):
        if key not in self.cache.keys():
            node = DLinkedList(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                removeNode = self.removeTail()
                self.cache.pop(removeNode.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.val = value
            self.moveToHead(node)

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def moveToHead(self, node):
        self.removeNode(node)
        self.addToHead(node)

    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node
