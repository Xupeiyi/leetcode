from TreeBuilder import TreeNode
from math import inf

class Solution0:

    def isValidBST(self, root):
        if not root:
            return True

        res_left = self.isValidBST(root.left)
        if not res_left:
            return False

        res_root = self.previous < root.val
        if not res_root:
            return False

        self.previous = root.val
        
        res_right = self.isValidBST(root.right)
        if not res_right:
            return False
        
        return True

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self._stack = []
        self._add(root)

    def _add(self, node):
        """节点入栈后，入栈左节点"""
        while node:
            self._stack.append(node)
            node = node.left

    def _pop(self):
        """节点出栈后，入栈右节点"""
        node = self._stack.pop(-1)
        self._add(node.right)
        return node.val

    def next(self) -> int:
        return self._pop()

    def hasNext(self) -> bool:
        return len(self._stack) > 0 

class Solution:

    def isValidBST(self, root):
        it = BSTIterator(root)
        prev = -inf
        while(it.hasNext()):
            v = it.next()
            if v <= prev:
                return False
            prev = v
        return True



if __name__ == '__main__':

    s = Solution()
    n0 = TreeNode(20)
    n1 = TreeNode(20)
    n2 = TreeNode(20)
    n3 = TreeNode(20, n1, n2)
    n4 = TreeNode(20, n0, n3)

    n4.display()
    print(s.isValidBST(n4))
