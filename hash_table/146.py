############################
# Solution 1: 借助标准库 中的 OrderedDict
############################

# Solution 2: 自己实现 OrderedDict


class Node:
    def __init__(self, key, value, prev=None, next_=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next_
        

# class DoublyLinkedList:
#     """不使用虚拟头尾节点"""
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def add_to_last(self, node):
#         node.prev = self.tail
#         node.next = None
#         self.tail = node
#         if not self.head:
#             self.head = self.tail
#         else:
#             self.tail.prev.next = self.tail
#
#     def move_to_end(self, node):
#         # node 不是尾节点
#         if node.next:
#             # 调整后一个节点
#             node.next.prev = node.prev
#
#             # 如果存在前一个节点，调整前一个节点
#             if node.prev:
#                 node.prev.next = node.next
#             else:
#                 self.head = node.next
#
#             node.prev = self.tail
#             node.next = None
#             self.tail.next = node
#             self.tail = node
#
#     def remove_first(self):
#         if self.head:
#             head = self.head.next
#             if head:
#                 head.prev = None
#             self.head = head
#
#     def __str__(self):
#         string = ''
#         curr = self.head
#         while curr:
#             string += f"{curr.key}: {curr.value}\n"
#             curr = curr.next
#
#         curr = self.head.prev
#         while curr:
#             string += f"{curr.key}: {curr.value}\n"
#             curr = curr.prev
#
#         return string


class DoublyLinkedList:
    """使用虚拟头尾节点"""
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_to_last(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        
    def move_to_end(self, node):
        if node.next is not self.tail:
            node.next.prev = node.prev
            node.prev.next = node.next
            self.add_to_last(node)
    
    def remove_first(self):
        first = self.head.next
        if first is not self.tail:
            first.prev.next = first.next
            first.next.prev = first.prev
    
    def __str__(self):
        string = ""
        curr = self.head.next
        while curr is not self.tail:
            string += f"{curr.key}: {curr.value}\n"
            curr = curr.next
        return string


class MyOrderedDict:
    
    def __init__(self):
        self._map = dict()
        self._list = DoublyLinkedList()
    
    def __getitem__(self, key):
        return self._map[key].value
    
    def __setitem__(self, key, value):
        if key not in self._map:
            node = Node(key, value)
            self._map[key] = node
            self._list.add_to_last(node)
        else:
            self._map[key].value = value
    
    def __len__(self):
        return len(self._map)
    
    def __contains__(self, item):
        return item in self._map
    
    def move_to_end(self, key):
        if key in self._map:
            self._list.move_to_end(self._map[key])
            
    def popitem(self, last):
        first_node = self._list.head.next
        if first_node:
            key = first_node.key
            self._map.pop(key)
            self._list.remove_first()
    
    def __str__(self):
        return str(self._list)


class LRUCache(MyOrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity
    
    def get(self, key) -> int:
        ans = -1
        if key in self:
            self.move_to_end(key)
            ans = self[key]
        return ans
        
    def put(self, key: int, value: int):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


if __name__ == '__main__':
    cache = LRUCache(2)
    
    od = MyOrderedDict()
    od['a'] = 1
    od['b'] = 2
    od['c'] = 3
    od.move_to_end('a')
    print(od)
    # print(len(od))
    od.popitem(False)
    print(od)
    
    # # instructions = ["put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
    # # args = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
    # instructions = ["put","put","get","put","get","put","get","get","get"]
    # args = [[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
    #
    # op = {"put": cache.put,
    #       "get": cache.get}
    #
    # for ins, arg in zip(instructions, args):
    #     print(ins + str(arg))
    #     try:
    #         op[ins](*arg)
    #     except:
    #         print(cache._map.keys())
    #         print(cache._list)
    #         break
    
    # ll = DoublyLinkedList()
    # n1 = Node(3, 4)
    # ll.add_to_last(n1)
    # n2 = Node(5, 6)
    # ll.add_to_last(n2)
    # n3 = Node(7, 8)
    # ll.add_to_last(n3)
    # print(ll)
    # ll.move_to_end(n1)
    # print(ll)
    # ll.move_to_end(n1)
    # print(ll)
    # ll.move_to_end(n3)
    # print(ll)
    # ll.remove_head()
    # print(ll)
    # ll.remove_head()
    # print(ll)
    # ll.remove_head()
    # print(ll)
    # ll.remove_head()
    # print(ll)
    
    #
    # lRUCache =  LRUCache(2)
    # lRUCache.put(1, 1)  # 缓存是 {1=1}
    # lRUCache.put(2, 2)  # 缓存是 {1=1, 2=2}
    # print(lRUCache.get(1))    # 返回 1
    # lRUCache.put(2, 3)  #
    # print(lRUCache.get(2))    # 返回 3 (未找到)
    # print(lRUCache.get(1))    # 返回 1
    # print(lRUCache.get(3))    # 返回 -1
    # print(lRUCache.get(4))    #返回 -1
    #
    
