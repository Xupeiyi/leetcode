from typing import List
from linkedlist import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        v_head = ListNode(0, head)

        i = 1
        curr = head
        prev = v_head
        insert_behind = prev
        while curr:
            if i <= left:
                insert_behind = prev
                curr = curr.next
                prev = prev.next
            elif left < i <= right:
                # pick out curr
                prev.next = curr.next
                # insert behind insert_behind
                curr.next = insert_behind.next
                insert_behind.next = curr
                curr = prev.next
            else:
                break
            i += 1
        return v_head.next


if __name__ == '__main__':
    s = Solution()

    n5 = ListNode(5)
    n4 = ListNode(4, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)

    ans = s.reverseBetween(n1, 3, 3)
    ans.print()