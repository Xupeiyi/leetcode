# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """extremely slow. because recursed twice"""
    def isBalanced(self, root: TreeNode) -> bool:
        def _isBalanced(root):
            if not root:
                return True, 0

            lbalanced, lheight = _isBalanced(root.left)
            rbalanced, rheight = _isBalanced(root.right)

            balanced = lbalanced and rbalanced and abs(lheight - rheight) <= 1
            height = max(lheight, rheight) + 1
            return balanced, height

        return _isBalanced(root)[0]


class Solution1:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(node):
            if node == None:
                return 0
            lheight = height(node.left)
            rheight = height(node.right)
            if lheight == -1 or rheight == -1 or abs(lheight - rheight) > 1:
                return -1
            else:
                return max(lheight, rheight) + 1
        return height(root) >= 0

_7 = TreeNode(7)
_6 = TreeNode(6)
_5 = TreeNode(5, _7, _6)
_4 = TreeNode(4)
_2 = TreeNode(2, _4, _5)
_3 = TreeNode(3)
_1 = TreeNode(1, _2)
print(Solution().isBalanced(_2))
print(Solution().isBalanced(_1))