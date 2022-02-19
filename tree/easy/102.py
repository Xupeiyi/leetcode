from TreeBuilder import TreeNode

class Solution:
    def levelOrder(self, root: TreeNode):
        levels = []
        if not root:
            return levels
        
        this_level = [root]
        while this_level:
            levels.append(this_level)
            
            next_level = []
            for node in this_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            this_level = next_level

        return [[node.val for node in level] for level in levels]

            
if __name__ == '__main__':
    s = Solution()

    n0 = TreeNode(7)
    n1 = TreeNode(2)
    n2 = TreeNode(11, n0, n1)
    n3 = TreeNode(4, n2)

    n6 = TreeNode(9)
    n7 = TreeNode(10)
    n4 = TreeNode(8, n7, n6)
    n5 = TreeNode(5, n3, n4)

    n5.display()
    print(s.levelOrder(n5))