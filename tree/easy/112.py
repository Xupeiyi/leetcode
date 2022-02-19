from TreeBuilder import TreeNode


class Solution:
    def hasPathSum(self, root:TreeNode, targetSum):
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum
        
        return self.hasPathSum(root.left, targetSum-root.val)\
            or self.hasPathSum(root.right, targetSum-root.val)

if __name__ == '__main__':
    s = Solution()

    n0 = TreeNode(7)
    n1 = TreeNode(2)
    n2 = TreeNode(11, n0, n1)
    n3 = TreeNode(4, n2)
    n5 = TreeNode(5, n3)

    n5.display()
    print(s.hasPathSum(n5, 22))



