from typing import Optional
from linkedlist import ListNode


# 这题折腾了两个小时...太弱小了，没有力量
# 要注意的地方好多， 之后做链表题不把图画清楚绝不动手
def mergesort(start, end):
    if start is end:
        return start, end

    # 这里出过bug: 
    # 如果写成 fast is not end.next and fast.next is not end.next,
    # 会在只有两个结点时让下文的start2 = end.next
    fast = start
    slow = start
    while fast is not end and fast.next is not end:
        fast = fast.next.next
        slow = slow.next

    # 这里出过bug: 
    # 在 mergesort(start, slow)之后， slow可能已经不再在原来的位置上了
    # 用 start2 提前保存slow.next2的位置作为第二次并归的头结点
    start2 = slow.next
    h1, t1 = mergesort(start, slow)
    h2, t2 = mergesort(start2, end)
    
    v_end = t2.next
    t1.next = v_end
    t2.next = v_end
    
    # 这里出过bug: 
    # v_head = ListNode(0, start)
    # 如果要插入在v_head后面的元素正好是start，就会导致start.next指向start自己
    v_head = ListNode(0, v_end)  
    insert_behind = v_head
    curr1 = h1
    curr2 = h2

    while curr1 is not v_end and curr2 is not v_end:
        if curr1.val < curr2.val:
            tmp = curr1
            curr1 = curr1.next
        else:
            tmp = curr2
            curr2 = curr2.next
        
        # 将 tmp 插入到insert_behind后面并更新insert_behind
        tmp.next = insert_behind.next
        insert_behind.next = tmp
        insert_behind = tmp
    
    if curr1 is not v_end:
        insert_behind.next = curr1
        end = curr1
    else:
        insert_behind.next = curr2
        end = curr2
    
    while end.next is not v_end:
        end = end.next
    
    return v_head.next, end  # 这里不小心写成v_end过 


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        tail = head
        while tail.next is not None:
            tail = tail.next

        start, _ = mergesort(head, tail)
        return start


if __name__ == '__main__':
    s = Solution()

    n5 = ListNode(1)
    n4 = ListNode(3, n5)
    n3 = ListNode(1, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(4, n2)

    ans = s.sortList(n1)
    ans.print()