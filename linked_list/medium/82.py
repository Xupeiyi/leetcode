from linkedlist import ListNode


def next_diff_val_node(head):
    while head:
        if head.next is None or head.next.val != head.val:
            return head.next
        head = head.next


# 思路一定要很清晰
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        v_head = ListNode()
        slow = v_head
        fast = head

        # 循环不变量：fast的值是从未出现过的
        # slow是当前结果的最后一个节点
        while fast:
            # fast指向最后一个结点，则直接添加
            if fast.next is None:
                slow.next = fast
                slow = slow.next
                break
            # fast的值不连续出现
            elif fast.next.val != fast.val:
                slow.next = fast
                fast = fast.next
                slow = slow.next
                continue
            else:
                fast = next_diff_val_node(fast)  # 使fast指向下一个未出现过的值
        slow.next = None
        return v_head.next


if __name__ == '__main__':
    s = Solution()

    n5 = ListNode(4)
    n4 = ListNode(3, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)

    ans = s.deleteDuplicates(n1)
    ans.print()