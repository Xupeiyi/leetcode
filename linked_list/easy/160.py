class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        i = headA
        j = headB
        while i != j:
            if i.next == j.next:
                return None
            i = i.next if i.next else headB
            j = j.next if j.next else headA
        return i
    
if __name__ == '__main__':
