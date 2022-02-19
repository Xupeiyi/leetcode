from TreeBuilder import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode):
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


if __name__ == '__main__':
    s = Solution()

    n3 = TreeNode(15)
    n2 = TreeNode(5)
    n1 = TreeNode(10, n2, n3)

    n5 = TreeNode(18)
    n4 = TreeNode(20, n1, n5)
    n4.display()
    print(s.preorderTraversal(n4))
