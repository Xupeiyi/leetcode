# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return str(self.val)
    

def printList(node):
    if not node:
        return
    print(str(node.val) + ' ')
    printList(node.next)


class Solution:
    def swapPairs(self, head: ListNode):
        if not head or not head.next:
            return head

        new_head = head.next
        head.next = self.swapPairs(new_head.next)
        new_head.next = head
        return new_head


if __name__ == '__main__':
    s = Solution()

    # n4 = ListNode(4)
    # n3 = ListNode(3, n4)
    # n2 = ListNode(2, n3)
    # n1 = ListNode(1, n2)
    # printList(n1)
    # head = s.swapPairs(n1)
    # printList(head)

    
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    printList(n1)
    head = s.swapPairs(n1)
    printList(head)
