from TreeBuilder import TreeNode


class Solution:
    path_cum = 0
    
    def convertBST(self, root):
        path_cum = 0
        
        def inorder(node):
            nonlocal path_cum
            if not node:
                return None
            
            right = inorder(node.right)
            path_cum += node.val
            val = path_cum
            left = inorder(node.left)
            return TreeNode(val, left, right)
        
        return inorder(root)
        

if __name__ == '__main__':
    s = Solution()
    
    n0 = TreeNode(0)
    n1 = TreeNode(2)
    n2 = TreeNode(1, n0, n1)
    ans = s.convertBST(n2)
    ans.display()
    
    n0 = TreeNode(1)
    n1 = TreeNode(2, n0)
    n2 = TreeNode(4)
    n3 = TreeNode(3, n1, n2)
    ans = s.convertBST(n3)
    ans.display()