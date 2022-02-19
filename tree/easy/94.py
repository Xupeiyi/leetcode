# Definition for a binary tree node.
class TreeNode:
    def __init__(self, name, val=0, left=None, right=None):
        self.name = name
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode):
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) 
        





if __name__ == '__main__':
    s = Solution()
    
    n3 = TreeNode('n3', 3)
    n2 = TreeNode('n2', 2, n3)
    n1 = TreeNode('n1', 1, None, n2)
    
    ans = s.inorderTraversal(n1)
    print(ans)