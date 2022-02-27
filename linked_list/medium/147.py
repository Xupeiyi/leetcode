from linkedlist import ListNode


def insert(head, tail, node):
    # 这个函数只能应对node.val < tail.val 的情况
    curr = head
    # curr.val 永远小于 node.val
    while curr is not tail:
        if curr.next.val > node.val:
            node.next = curr.next
            curr.next = node
            break
        curr = curr.next



class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head

        v_head = ListNode(-5001, head) 
        curr = head.next
        tail = head
        while curr:
            # 不要试图让一个函数应对所有的情况，先分类，然后写功能单一的函数
            if curr.val < tail.val:
                tmp = curr
                curr = curr.next
                tail.next = curr
                insert(v_head, tail, tmp)
            else:
                tail = curr
                curr = curr.next
        return v_head.next


if __name__ == '__main__':
    s = Solution()
    n5 = ListNode(1)
    n4 = ListNode(3, n5)
    n3 = ListNode(1, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(4, n2)

    ans = s.insertionSortList(n1)
    ans.print()