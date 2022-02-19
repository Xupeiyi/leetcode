from TreeBuilder import TreeNode


def children(node, seq):
    return [n for n in (node.right, node.left)[::seq] if n] 

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return []

        seq = 1
        level = [root]
        ans = []

        while level:
            next_level = []
            for node in reversed(level):
                next_level += children(node, seq)

            ans.append([node.val for node in level])
            seq *= -1
            level = next_level
        
        return ans


if __name__ == '__main__':
    f = Solution().zigzagLevelOrder

    n0 = TreeNode(9)
    n1 = TreeNode(15)
    n2 = TreeNode(7)
    n3 = TreeNode(20, n1, n2)
    n4 = TreeNode(3, n0, n3)

    n4.display()
    print(f(n4))
            
            