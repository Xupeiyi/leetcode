# Definition for a binary tree node.

class TreeNode:
    def __init__(self, name, val=0, left=None, right=None):
        self.name = name
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



if __name__ == '__main__':
    s = Solution()
    
    n3 = TreeNode('n3', 15)
    n2 = TreeNode('n2', 5)
    n1 = TreeNode('n1', 10, n2, n3)

    n4 = TreeNode('n4', 15)
    n5 = TreeNode('n5', 5, None, n4)
    n6 = TreeNode('n6', 10, n5)
    

    print(s.isSameTree(n1, n6))