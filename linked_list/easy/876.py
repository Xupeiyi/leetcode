class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        i = j = head
        i_idx = 0
        while i.next is not None:
            i = i.next
            i_idx += 1
            if i_idx % 2:
                j = j.next
        return j


if __name__ == '__main__':
    s = Solution()

    n1 = ListNode(5)
    n2 = ListNode(4, n1)
    n3 = ListNode(3, n2)
    n4 = ListNode(2, n3)
    n5 = ListNode(1, n4)

    print(s.middleNode(n5).val)