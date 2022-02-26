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