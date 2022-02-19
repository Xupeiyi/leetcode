from TreeBuilder import TreeNode

class Solution:

    def minDepth0(self, root):
        "my original solution"
        if not root:
            return 0
            
        if not root.left and not root.right:
            return 1
        
        shortest = []
        if root.left:
            shortest.append(self.minDepth(root.left))
        
        if root.right:
            shortest.append(self.minDepth(root.right))

        return 1 + min(shortest)


    def minDepth(self, root: TreeNode) -> int:
        "modified solution"
        if not root:
            return 0

        # if is a leaf node
        if not root.left and not root.right:
            return 1

        shortest_left = self.minDepth(root.left)
        shortest_right = self.minDepth(root.right)

        return 1 + min(shortest_left, shortest_right) if root.left and root.right \
            else 1 + shortest_left + shortest_right


if __name__ == '__main__':
    s = Solution()

    n0 = TreeNode(14)
    n1 = TreeNode(13, None, n0)
    # n2 = TreeNode(10)
    n4 = TreeNode(12, None, n1)

    ans = s.minDepth(n4)
    print(ans)





