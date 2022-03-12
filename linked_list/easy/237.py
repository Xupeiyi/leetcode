
# 借用评论区一句话：如何让自己在世界上消失，但又不死？ 
# 将自己完全变成另一个人，再杀了那个人就行了。
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
