from TreeBuilder import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

if __name__ == '__main__':
    s = Solution()

    n0 = TreeNode(0)
    n1 = TreeNode(1)
    n2 = TreeNode(2, n0, n1)
    n2.display()
    ans = s.invertTree(n2)
    ans.display()


    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5, n3, n4)
    n6 = TreeNode(6, n2, n5)
    n6.display()
    s.invertTree(n6).display()
