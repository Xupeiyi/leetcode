from linkedlist import ListNode


class Solution:
    
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None

        v_head = ListNode(0, head)  # 虚拟头结点

        # 找到第一个值小于 x 的结点，作为插入新结点的位置
        insert_behind = v_head
        while insert_behind.next.val < x:
            insert_behind = insert_behind.next
            if not insert_behind.next:
                return v_head.next

        curr = insert_behind.next
        while curr.next:
            if curr.next.val < x:
                tmp = curr.next
                # 将tmp从链表中拿出来
                curr.next = curr.next.next

                # 将tmp添加到insert_behind之后， 并成为新的insert_behind
                tmp.next = insert_behind.next
                insert_behind.next = tmp
                insert_behind = insert_behind.next
            else:
                curr = curr.next
        return v_head.next


if __name__ == '__main__':
    s = Solution()

    n5 = ListNode(1)
    n4 = ListNode(8, n5)
    n3 = ListNode(1, n4)
    n2 = ListNode(1, n3)
    n1 = ListNode(1, n2)

    ans = s.partition(n1, 3)
    ans.print()