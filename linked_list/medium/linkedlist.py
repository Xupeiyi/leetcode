class ListNode:
    _id = 0
    
    def __repr__(self):
        return f"val={self.val}, id={self.id}"

    def __init__(self, val=0, next=None):
        self.id = -self.__class__._id
        self.__class__._id -= 1

        self.val = val
        self.next = next

    def print(self):
        s = ""
        curr = self
        while curr:
            s += str(curr.val) + "->"
            curr = curr.next
        print(s)