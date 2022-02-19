from TreeBuilder import TreeNode


def children(node):
    return [n for n in (node.left, node.right) if n]


class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []

        ans = []
        level = [root]
        while level:
            next_level = []

            for node in level:
                next_level += children(node)

            ans.insert(0, [node.val for node in level])
            level = next_level
        return ans

if __name__ == '__main__':
    f = Solution().levelOrderBottom

    n0 = TreeNode(9)
    n1 = TreeNode(15)
    n2 = TreeNode(7)
    n3 = TreeNode(20, n1, n2)
    n4 = TreeNode(3, n0, n3)

    n4.display()
    print(f(n4))


        