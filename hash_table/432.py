class Node:
    def __init__(self, key="", count=0):
        self.prev = None
        self.next = None
        self.keys = {key}
        self.count = count
    
    def insert(self, node):
        # 在self后插入node
        node.prev = self
        node.next = self.next
        node.prev.next = node
        node.next.prev = node
        return node
    
    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
    

class AllOne:

    def __init__(self):
        self.root = Node()
        self.root.prev = self.root
        self.root.next = self.root
        self.nodes = {}
    
    def inc(self, key):
        if key not in self.nodes:
            # 链表为空，或没有count=1的结点
            if self.root.next is self.root or self.root.next.count > 1:
                self.nodes[key] = self.root.insert(Node(key, 1))
            else:
                self.root.next.keys.add(key)
                self.nodes[key] = self.root.next
        else:
            curr = self.nodes[key]
            nxt = curr.next
            if nxt is self.root or nxt.count > curr.count + 1:
                self.nodes[key] = curr.insert(Node(key, curr.count+1))
            else:
                nxt.keys.add(key)
                self.nodes[key] = nxt
            curr.keys.remove(key)
            if len(curr.keys) == 0:
                curr.remove()
    
    def dec(self, key):
        curr = self.nodes[key]
        if curr.count == 1:
            del self.nodes[key]
        else:
            prev = curr.prev
            if prev is self.root or prev.count < curr.count - 1:
                self.nodes[key] = curr.prev.insert(Node(key, curr.count-1))
            else:
                prev.keys.add(key)
                self.nodes[key] = prev
        curr.keys.remove(key)
        if len(curr.keys) == 0:
            curr.remove()
    
    def getMaxKey(self):
        return next(iter(self.root.prev.keys)) if self.root.prev is not self.root else ""
    
    def getMinKey(self):
        return next(iter(self.root.next.keys)) if self.root.next is not self.root else ""


    

