# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def symmetric_equal(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        
        return left.val == right.val\
               and self.symmetric_equal(left.left, right.right)\
               and self.symmetric_equal(left.right, right.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.symmetric_equal(root.left, root.right)


if __name__ == '__main__':
    s = Solution()

    n1 = TreeNode(3)
    n2 = TreeNode(4)
    n3 = TreeNode(2, n1, n2)

    n4 = TreeNode(4)
    n5 = TreeNode(3)
    n6 = TreeNode(2, n4, n5)

    n7 = TreeNode(1, n3, n6)

    print(s.isSymmetric(n7))






