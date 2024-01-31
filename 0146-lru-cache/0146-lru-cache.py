class Node:
    def __init__ (self, val,key):
        self.next = self.prev = None
        self.val = val
        self.key = key
class LRUCache:

    def __init__(self, capacity: int):
        self.rightNode = self.leftNode = Node(0,0)
        self.rightNode.next, self.leftNode.prev = self.leftNode, self.rightNode
        self.lookup = {}
        self.capacity = capacity
    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        self.remove(self.lookup[key])
        self.insert(self.lookup[key])
        return self.lookup[key].val
    
    def put(self, key: int, value: int) -> None:
        newNode = Node(value, key)
        if key in self.lookup:
            self.remove(self.lookup[key])
        self.lookup[key] = newNode
        self.insert(newNode)
        if len(self.lookup) > self.capacity:
            lru = self.leftNode.next
            self.remove(lru)
            del self.lookup[lru.key]
            
            
    def insert(self, node:Node) -> None:
        #always insert next to rightNode
        prv = self.rightNode.prev
        nxt = self.rightNode
        prv.next = nxt.prev = node
        node.next,node.prev = nxt, prv
        
    def remove(self, node:Node)-> None:
        prv,nxt = node.prev, node.next
        prv.next,nxt.prev = nxt, prv

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)