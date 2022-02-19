"""
核心在于认识到链表值得顺序是由对树进行中序遍历得到的。
如何根据中序遍历的顺序还原树？
"""

from TreeBuilder import TreeNode

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None

        # find the length of linked list
        length = 0
        h = head
        while h:
            length += 1
            h = h.next
        
        def buildBST(start, end):
            nonlocal head
            if start > end:
                return None
            mid = (start + end) // 2
            left = buildBST(start, mid - 1)
            root = TreeNode(head.val, left)
            head = head.next
            root.right = buildBST(mid + 1, end)
            return root

        return buildBST(0, length - 1)

if __name__ == '__main__':
    s = Solution()

    n0 = ListNode(6)
    n1 = ListNode(5, n0)
    n2 = ListNode(4, n1)
    n3 = ListNode(3, n2)
    n4 = ListNode(2, n3)
    n5 = ListNode(1, n4)

    s.sortedListToBST(n5).display()




