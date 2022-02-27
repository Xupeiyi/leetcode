from linkedlist import ListNode

class Node(ListNode):
    def __init__(self, x, next=None, random=None):
        super().__init__(x, next)
        self.random = random



class Solution:
    
    clone = {None: None}
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        if head not in self.clone:
            self.clone[head] = Node(head.val)
        if head.random not in self.clone:
            self.clone[head.random] = Node(head.random.val)

        new_head = self.clone[head]
        new_head.random = self.clone[head.random]
        new_head.next = self.copyRandomList(head.next)
        return new_head
