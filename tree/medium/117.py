from TreeBuilder import TreeNode


class Node(TreeNode):
    def __init__(self, val, left=None, right=None, next=None):
        super().__init__()
        self.next = next
        

class Solution:
    def connect(self, root):
        """不断利用上一次迭代的结果"""
        curr = root
        
        while curr:
            head = tail = Node(0)  # virtual head/tail for next level
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                
                curr = curr.next
            curr = head.next
            
        return root
        