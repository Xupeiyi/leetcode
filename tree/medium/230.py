# ------------------------------------
# Solution1
from TreeBuilder import TreeNode

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


class Solution1:
    def kthSmallest(self, root: TreeNode, k: int):
        it = BSTIterator(root)
        for i in range(0, k):
            res = it.next()
        return res


# ---------------------------------------
# Solution2


class Solution:
    
    def kthSmallest(self, root, k: int) -> int:
        rank = 0
        ans = 0
        
        def inorder(node):
            nonlocal rank
            nonlocal ans
            if not node:
                return
        
            inorder(node.left)
            rank += 1
            if rank > k:
                return
            elif rank == k:
                ans = node.val
                return
            inorder(node.right)
        
        inorder(root)
        return ans


if __name__ == '__main__':
    s = Solution()

    n0 = TreeNode(3)

    n1 = TreeNode(12)
    n2 = TreeNode(20)
    n3 = TreeNode(15, n1, n2)
    
    n4 = TreeNode(10, n0, n3)

    n4.display()
    ans = s.kthSmallest(n4, 1)
    print(ans)
    