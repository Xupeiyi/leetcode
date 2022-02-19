from TreeBuilder import TreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode):
        if not root:
            return []
        return self.postorderTraversal(root.left) \
            + self.postorderTraversal(root.right) \
            + [root.val]

if __name__ == '__main__':
    s = Solution()

    n0 = TreeNode(3)
    n1 = TreeNode(2, n0)
    n2 = TreeNode(1, None, n1)

    print(s.postorderTraversal(n2))

  