class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print(self):
        s = ""
        curr = self
        while curr:
            s += str(curr.val) + "->"
            curr = curr.next
        print(s)


class Solution:
    def rotateRight(self, head, k: int):
        if not head or not head.next:
            return head
        
        # 获得链表长度，同时将链表连接成环
        curr = head
        length = 1
        while curr.next:
            length += 1
            curr = curr.next
        curr.next = head
        
        # 将第length - n % length个结点与之后的结点断开
        node_idx = 1
        curr = head
        while node_idx < length - k % length:
            curr = curr.next
            node_idx += 1
        new_head = curr.next
        curr.next = None
        return new_head
        
        
if __name__ == '__main__':
    s = Solution()
    
    n1 = ListNode(5)
    n2 = ListNode(4, n1)
    n3 = ListNode(3, n2)
    n4 = ListNode(2, n3)
    n5 = ListNode(1, n4)
    
    ans = s.rotateRight(n5, 2)
    ans.print()
    
    
    n1 = ListNode(2)
    n2 = ListNode(1, n1)
    n3 = ListNode(0, n2)
    ans = s.rotateRight(n3, 4)
    ans.print()