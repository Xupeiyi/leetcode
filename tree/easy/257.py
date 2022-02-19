from TreeBuilder import TreeNode


class Solution:
    def binaryTreePaths(self, root):
        paths = []
        
        def dfs(node, path):
            nonlocal paths
            if node:
                if not node.left and not node.right:
                    paths.append("->".join(path + [str(node.val)]))
                else:
                    dfs(node.left, path + [str(node.val)])
                    dfs(node.right, path + [str(node.val)])
                
        dfs(root, [])
        return paths

  
if __name__ == '__main__':
    n0 = TreeNode(4)
    n1 = TreeNode(5)
    n2 = TreeNode(2, n0, n1)
    
    n3 = TreeNode(6)
    n4 = TreeNode(3, n3)
    
    n5 = TreeNode(1, n2, n4)
    n5.display()
    
    s = Solution()

    print(s.binaryTreePaths(n5))