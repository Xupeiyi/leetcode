from TreeBuilder import TreeNode
from math import inf

class Solution:
    def recoverTree(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        previous = TreeNode(-inf)
        downwards = []
        def inorder(node):
            nonlocal previous
            nonlocal downwards
            if not node:
                return
            
            inorder(node.left)
            
            if node.val < previous.val:
                downwards += [previous, node]
            
            previous = node

            inorder(node.right)

        inorder(root)
        swap0, swap1 = downwards[0], downwards[-1]
        swap0.val, swap1.val = swap1.val, swap0.val


if __name__ == '__main__':
    s = Solution()

    n0 = TreeNode(15)

    n1 = TreeNode(12)
    n2 = TreeNode(20)
    n3 = TreeNode(3, n1, n2)
    
    n4 = TreeNode(10, n0, n3)

    n4.display()
    s.recoverTree(n4)
    n4.display()


            

