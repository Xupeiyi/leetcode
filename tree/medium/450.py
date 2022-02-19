from TreeBuilder import TreeNode


def getMin(root):
    if not root.left:
        return root
    return getMin(root.left)


class Solution:
    def deleteNode(self, root, key: int):
        if not root:
            return None

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            
            if not root.right:
                return root.left
            
            minNode = getMin(root.right)
            root.right = self.deleteNode(root.right, minNode.val)
            minNode.left = root.left
            minNode.right = root.right
            root = minNode
        
        return root


if __name__ == '__main__':
    s = Solution()
    
    n3 = TreeNode(3)
    n0 = TreeNode(0, n3)
    n1 = TreeNode(2)
    n2 = TreeNode(1, n0, n1)
    n2.display()
    ans = s.deleteNode(n2, 0)
    ans.display()
    
    n0 = TreeNode(1)
    n1 = TreeNode(2, n0)
    n2 = TreeNode(4)
    n3 = TreeNode(3, n1, n2)
    n3.display()
    ans = s.deleteNode(n3, 3)
    ans.display()
    
    n3 = TreeNode(-1)
    n0 = TreeNode(0, n3)
    n1 = TreeNode(2)
    n2 = TreeNode(1, n0, n1)
    n2.display()
    ans = s.deleteNode(n2, -1)
    ans.display()