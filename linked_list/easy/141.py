class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head.next
        
        if not slow:
            return False
        
        fast = head.next.next
        while fast:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
            
        return False
    