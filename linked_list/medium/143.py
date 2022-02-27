from linkedlist import ListNode


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []

        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next

        curr = head
        tail = stack.pop()
        while curr is not tail and curr.next is not tail:
            tail.next = curr.next
            curr.next = tail
            curr = curr.next.next
            tail = stack.pop()

        tail.next = None


if __name__ == '__main__':
    s = Solution()
    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)

    s.reorderList(n1)
    n1.print()