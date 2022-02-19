from TreeBuilder import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode):
        ans = []
        if not root:
            return ans
        
        level = [root]
        while level:
            ans.append(level[-1].val)
            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level
        
        return ans
    
if __name__ == '__main__':
    s = Solution()
    
    n0 = TreeNode(1)
    n1 = TreeNode(2)
    n2 = TreeNode(3, n0, n1)
    
    n3 = TreeNode(4)
    
    n5 = TreeNode(6, n3)
    
    n6 = TreeNode(7, n2, n5)
    
    ans = s.rightSideView(n6)
    print(ans)